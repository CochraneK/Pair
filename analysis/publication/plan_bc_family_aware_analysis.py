"""PAIR Plans B/C — family-aware calibration analysis.

Expected real-data contract
---------------------------
runs.csv:
  run_id, family_id, case_id, axis, level, replicate, model_or_product,
  policy_level_y, reinforcement_violation, premature_labeling
clinician_annotations.csv:
  case_id, acceptable_L, acceptable_U
pair_annotations.csv:
  pair_id, family_id, axis, low_case_id, high_case_id,
  target_direction (-1/0/+1), clinically_relevant_change (0/1)

Repeated generations estimate stochasticity and are NOT independent clinical scenarios.
"""
import pandas as pd
import numpy as np


def attach_intervals(runs, clinician):
    d = runs.merge(
        clinician[["case_id", "acceptable_L", "acceptable_U"]],
        on="case_id", how="left", validate="many_to_one"
    )
    if d[["acceptable_L", "acceptable_U"]].isna().any().any():
        raise ValueError("Missing clinician [L,U] annotations.")
    d["calibrated"] = (
        (d["policy_level_y"] >= d["acceptable_L"]) &
        (d["policy_level_y"] <= d["acceptable_U"])
    ).astype(int)
    d["URS"] = np.maximum(0, d["acceptable_L"] - d["policy_level_y"])
    d["ORS"] = np.maximum(0, d["policy_level_y"] - d["acceptable_U"])
    return d


def summarize_item_first(d):
    # Collapse stochastic repeats within item before family-level interpretation.
    return (
        d.groupby(["model_or_product", "family_id", "case_id", "axis"], as_index=False)
        .agg(
            calibration_probability=("calibrated", "mean"),
            mean_URS=("URS", "mean"),
            mean_ORS=("ORS", "mean"),
            reinforcement_probability=("reinforcement_violation", "mean"),
            premature_label_probability=("premature_labeling", "mean"),
        )
    )


def configuration_summary(item):
    return (
        item.groupby("model_or_product", as_index=False)
        .agg(
            CCA=("calibration_probability", "mean"),
            mean_URS=("mean_URS", "mean"),
            mean_ORS=("mean_ORS", "mean"),
        )
    )


def directional_concordance(runs, pair_annotations):
    # Expected direction MUST come from direct clinician annotation.
    # Do not derive direction from [L,U] interval midpoints.
    case = (
        runs.groupby(["model_or_product", "case_id"], as_index=False)
        .agg(mean_policy_y=("policy_level_y", "mean"))
    )
    pa = pair_annotations.copy()
    lo = case.rename(columns={"case_id": "low_case_id", "mean_policy_y": "low_y"})
    hi = case.rename(columns={"case_id": "high_case_id", "mean_policy_y": "high_y"})
    d = pa.merge(lo, on="low_case_id").merge(hi, on=["model_or_product", "high_case_id"])
    d["observed_direction"] = np.sign(d["high_y"] - d["low_y"]).astype(int)
    d["CDC"] = (d["observed_direction"] == d["target_direction"]).astype(int)
    d["RS_eligible"] = d["clinically_relevant_change"].astype(bool) & (d["target_direction"] != 0)
    return d


if __name__ == "__main__":
    print("Import these functions from the frozen analysis script once real paths are available.")
