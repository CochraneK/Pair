#!/usr/bin/env Rscript

# PAIR Plan A confirmatory analysis candidate
# Freeze before real outcome data are inspected.

suppressPackageStartupMessages({
  library(readr)
  library(dplyr)
  library(ordinal)
  library(emmeans)
  library(ggplot2)
})

args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 2) stop("Usage: Rscript analysis/plan_a_analysis.R ratings.csv outdir")
input <- args[[1]]
outdir <- args[[2]]
dir.create(outdir, recursive = TRUE, showWarnings = FALSE)

d <- read_csv(input, show_col_types = FALSE)

required <- c("appropriateness_0_2","condition","product_id","sips_domain","pair_id","prompt_id")
missing <- setdiff(required, names(d))
if (length(missing)) stop(paste("Missing columns:", paste(missing, collapse=", ")))

d <- d %>%
  mutate(
    appropriateness = ordered(appropriateness_0_2, levels=c(0,1,2)),
    condition = factor(condition, levels=c("control","psychotic")),
    product_id = factor(product_id),
    sips_domain = factor(sips_domain),
    pair_id = factor(pair_id),
    prompt_id = factor(prompt_id)
  )

# Primary candidate model. If raw multiple-rater rows are used directly,
# add rater structure or switch input to the frozen adjudicated outcome.
m <- clmm(
  appropriateness ~ condition * product_id + sips_domain +
    (1|pair_id) + (1|prompt_id),
  data=d,
  link="logit",
  Hess=TRUE,
  nAGQ=1
)

capture.output(summary(m), file=file.path(outdir,"plan_a_clmm_summary.txt"))

# Marginal probabilities by condition/product.
emm <- emmeans(m, ~ condition | product_id, mode="prob")
write_csv(as.data.frame(emm), file.path(outdir,"plan_a_marginal_probabilities.csv"))

# Condition contrasts within product.
ctr <- contrast(emm, method="revpairwise", by="product_id")
write_csv(as.data.frame(ctr), file.path(outdir,"plan_a_condition_contrasts.csv"))

# Descriptive score-2 probability.
desc <- d %>%
  group_by(product_id, condition, sips_domain) %>%
  summarise(n=n(), score2_rate=mean(as.integer(as.character(appropriateness))==2, na.rm=TRUE), .groups="drop")
write_csv(desc, file.path(outdir,"plan_a_score2_descriptives.csv"))

# Plot model-independent score-2 profile for QA/reporting.
p <- ggplot(desc, aes(x=sips_domain, y=score2_rate, group=condition, linetype=condition)) +
  geom_point() + geom_line() + facet_wrap(~product_id) +
  labs(x="SIPS domain", y="Observed score-2 proportion", title="PAIR Plan A failure profile") +
  theme_minimal()
ggsave(file.path(outdir,"plan_a_score2_profile.png"), p, width=10, height=6, dpi=160)

writeLines(capture.output(sessionInfo()), file.path(outdir,"sessionInfo.txt"))
cat("Plan A analysis completed\n")
