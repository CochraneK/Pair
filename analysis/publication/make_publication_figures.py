"""PAIR publication-figure generator.

This file defines the figure layer; it is designed to consume analysis-ready
summary tables created from frozen REAL analyses. Synthetic rehearsal figures
are for layout and manuscript testing only.
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

TABLES = Path("tables")
FIGURES = Path("figures")
FIGURES.mkdir(exist_ok=True)

# Plan A example: paired binary sensitivity forest.
d = pd.read_csv(TABLES / "A_paired_binary_sensitivity.csv").sort_values("paired_risk_difference_pp")
y = np.arange(len(d))
plt.figure(figsize=(8.2, 4.8))
plt.errorbar(
    d["paired_risk_difference_pp"], y,
    xerr=[d["paired_risk_difference_pp"] - d["rd_ci_low_pp"],
          d["rd_ci_high_pp"] - d["paired_risk_difference_pp"]],
    fmt="o", capsize=4
)
plt.axvline(0, linewidth=1)
plt.yticks(y, d["product"])
plt.xlabel("Paired risk difference (percentage points)")
plt.title("Psychosis-related minus matched-control inappropriate-response risk")
plt.tight_layout()
plt.savefig(FIGURES / "A_paired_risk_difference.png", dpi=300, bbox_inches="tight")
plt.close()

# Additional manuscript figures should be generated from the frozen output
# tables for: ordinal category probabilities, repeat stability, failure profiles,
# B/C CCA versus directional concordance, URS versus ORS, and axis-level maps.
