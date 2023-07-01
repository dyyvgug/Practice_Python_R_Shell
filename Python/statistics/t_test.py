from scipy import stats
import numpy as np
# ------------------------------------------------------------------
# One-Sample T-Test
# ------------------------------------------------------------------
print("one sample t test")
rvs = [61,72,56,49,43,37,80,89,92,97,75,73,35,47,45,67,60,77,76,62,43,39]
mean = np.mean(rvs)
std = np.std(rvs)
print("mean:", mean, "\tstd:",std)

t,p = stats.ttest_1samp(rvs,70)
print("t value:",t,"\tp value:",p)

# -----------------------------------------------------------------
# paired-samples t-test
# -----------------------------------------------------------------
print("\npaired samples t-test")
x = [19.7,21.2,20.7,18.6,17.4,19.3,20.7]
y = [20.5,19.7,18.7,19.1,17.1,21.0,19.5]

t,p = stats.ttest_rel(x,y)
print("t value:",t,"\tp value:",p)

