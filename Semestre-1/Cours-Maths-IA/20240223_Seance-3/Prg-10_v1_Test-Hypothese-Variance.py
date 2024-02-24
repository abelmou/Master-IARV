from scipy import stats

data = [2.5, 3.2, 2.8, 3.5, 3, 3.2, 2.9, 3.4, 3.1, 2.7, 3.3, 2.6, 3.6, 3, 3.1, 3.3, 2.9, 3.2, 3.4, 3.1]

t_stat, p_value = stats.ttest_1samp(data, 3)
print("Test t de Student :", t_stat)
print("p_value :", p_value)