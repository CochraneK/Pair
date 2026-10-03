# PAIR Plan A — primary confirmatory analysis
# Requires R packages: ordinal, emmeans, dplyr, readr
# Intended for REAL data. Synthetic rehearsal outputs do not replace this model.

library(readr)
library(dplyr)
library(ordinal)
library(emmeans)

runs <- read_csv("data/A_RUNS_REAL.csv", show_col_types = FALSE)
ratings <- read_csv("data/A_RATINGS_ADJUDICATED_REAL.csv", show_col_types = FALSE)

dat <- runs %>%
  filter(phase == "primary") %>%
  inner_join(ratings, by = "run_id") %>%
  mutate(
    appropriateness = ordered(appropriateness_0_2, levels = c(0,1,2)),
    condition = factor(condition, levels = c("control","psychotic")),
    product_id = factor(product_id),
    sips_domain = factor(sips_domain),
    pair_id = factor(pair_id),
    prompt_id = factor(case_id)
  )

# Freeze this exact random-effects structure before outcome analysis.
m_primary <- clmm(
  appropriateness ~ condition * product_id + sips_domain +
    (1 | pair_id) + (1 | prompt_id),
  data = dat,
  link = "logit",
  Hess = TRUE
)

print(summary(m_primary))

# Prespecified overall psychosis-vs-control contrast.
emm <- emmeans(m_primary, ~ condition)
print(pairs(emm, reverse = TRUE))

# Model-based category probabilities by product and condition.
prob <- emmeans(m_primary, ~ condition | product_id, mode = "prob")
write.csv(as.data.frame(prob), "results/A_model_probabilities.csv", row.names = FALSE)

# Prespecified sensitivity analysis excluding P5 disorganized communication.
m_no_p5 <- update(m_primary, data = filter(dat, sips_domain != "P5"))
print(summary(m_no_p5))
