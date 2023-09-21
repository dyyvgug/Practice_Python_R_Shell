import scipy.stats as stats
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
from scipy.stats import f_oneway

# ================================================================================================
# recall T-test,U-test,X2-test,F-test. Yingying Dong.
# T-test compares means of two groups with assumptions of normality and equal variances.
# U-test compares distributions of two groups without assuming a specific distribution.
# Chi-Square test(X2-test) assesses associations between categorical variables.
# Variance test (F-test) compares variability between groups and is commonly used in ANOVA.
# ================================================================================================

# =================================================================
# T-test
# =================================================================
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

# -----------------------------------------------------------------------------------------
# The paired-samples t-test
# such as one machine processes products with radius x and y at two different temperature,
# then check if it is a significant difference
# -----------------------------------------------------------------------------------------
print("\npaired samples t-test")
x = [19.7,21.2,20.7,18.6,17.4,19.3,20.7]
y = [20.5,19.7,18.7,19.1,17.1,21.0,19.5]

t,p = stats.ttest_rel(x,y)
print("t value:",t,"\tp value:",p)
# p value > 0.05， no significant difference

# --------------------------------------------------------------------------------------------------
# The two independent samples t-test
# such as two machines process same type products, machine a with a radius, machine b with b radius,
# then check if is there a significant difference between two machines.
# --------------------------------------------------------------------------------------------------
print('\ntwo independent samples t-test')
a = [34.2,42.3,32.9,29.3,28.9,27.7,39.5,40.1]
b = [40.5,33.2,40.3,32.9,37.5,29.7,28.9]

t,p = stats.ttest_ind(a,b)
print("t value:",t,"\tp value:",p)
# p value > 0.05， no significant difference

# ===============================================================================
# U-test
# ===============================================================================
# scipy.stats.mannwhitneyu(x, y, use_continuity=True, alternative='two-sided', axis=0, method='auto', *, nan_policy='propagate', keepdims=False)
print("\nU-test")
x = [134,146,104,172,196,147,96,105]
y = [94,163,156,174,89,99,119]
u,p = stats.mannwhitneyu(x,y,alternative='two-sided')
print("U value:",u,"\tp value:",p)

# ===============================================================================
# Chi-square (X2) test
# test if there is an association between two categorical variables:
#   "Gender" (Male or Female) and "Preference" (Option A, Option B, or Option C).
# ===============================================================================
print("\nChi-Square(X2) test")
data = {
'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
'Preference': ['Option A', 'Option B', 'Option B', 'Option C', 'Option A', 'Option B', 'Option C', 'Option A']
}
df = pd.DataFrame(data)
contingency_table = pd.crosstab(df['Gender'],df['Preference'])
print("Contingency Table:\n",contingency_table)

chi2,p,dof,expected = chi2_contingency(contingency_table)
print("\nChi-Square test statistic:",chi2)
print("\np value:",p)
print("\nDegrees of freedom:",dof)
print("\nExpected frequencies table:")
print(pd.DataFrame(expected,index=df['Gender'].unique(),columns=df['Preference'].unique()))

alpha = 0.05
if p < alpha:
    print("\nThere is a significant association between Gender and Preference")
else:
    print("\nThere is no significant association between Gender and Preference")
# ================================================================================
# Variance test (F-test)
# Let's check if there is a significant difference in the variance of the exam scores
#  among the three groups.
# ================================================================================
print("\n F-test (variance test)")

group1_scores = [85, 90, 88, 92, 87]
group2_scores = [78, 82, 80, 85, 80]
group3_scores = [95, 92, 90, 96, 94]

f,p = f_oneway(group1_scores,group2_scores,group3_scores)
print("\n F-test statistic:",f)
print("p value:",p)

if p < alpha:
    print("\nThere is a significant difference in the variance of exam scores among the three groups.")
else:
    print("\nThere is no significant difference in the variance of exam scores among the three groups.")
