from scipy.stats import ttest_ind

# Sample data: Study hours and exam scores
group_1 = [55, 60, 65, 70, 75, 80, 85, 90]  # Studied less
group_2 = [70, 75, 80, 85, 90, 95, 100, 100]  # Studied more

# Perform T-test
t_stat, p_value = ttest_ind(group_1, group_2)

print("T-Statistic:", t_stat)
print("P-Value:", p_value)

# Interpretation
if p_value < 0.05:
    print("The difference is statistically significant (Studying helps!).")
else:
    print("The difference is NOT statistically significant (Might be random).")
