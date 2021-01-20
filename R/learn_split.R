# learning split(). Yingying Dong.
# dividing data in groups based on factor levels.

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
# ====================================================================
# Split vector
# ====================================================================
a <- c(x = 3, y = 5, x = 1, x = 4, y = 3)
a
split(a, f = names(a))

# character vector
groups <- c("Group 1", "Group 1", "Group 2", "Group 1", "Group 2")
split(a, f = groups)
split(a, f = factor(groups)) # Equivalent

# by multiple groups
groups2 <- c("Type 1", "Type 1", "Type 1", "Type 2", "Type 1")
split(a, f = list(groups, groups2))
# Equivalent
f1 <- factor(c("Group 1", "Group 1", "Group 2", "Group 1", "Group 2"),
             levels = c("Group 1", "Group 2"))
f2 <- factor(c("Type 1", "Type 1", "Type 1", "Type 2", "Type 1"),
             levels = c("Type 1", "Type 2"))
split(a, f = list(f1, f2))
# group interactions are separated with customization
vec_split <- split(a, f = list(f1, f2), drop = TRUE, sep = ": ")
vec_split

# =====================================================================
# Split data frame
# =====================================================================
set.seed(3)

df <- CO2[sample(1:nrow(CO2), 10), ]
head(df)

# for treatment group
split(df, f = df$Treatment)
# for type and treatment groups
dfs <- split(df, f = list(df$Type, df$Treatment))
dfs

# recover the original data frame
unsplit(dfs, f = list(df$Type, df$Treatment))
