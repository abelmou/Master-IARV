from scipy import stats

data = [9.8, 10.2, 10, 10.1, 9.9, 10.3, 9.7, 9.8, 10.2, 10.1, 10, 9.9, 10.3, 9.7, 9.8, 10.2, 10.1, 10, 9.9, 10.3, 9.7, 9.8, 10.2, 10.1, 10, 9.9, 10.3, 9.7, 9.8, 10.2]

t_stat, p_value = stats.ttest_1samp(data, 10)
print("Test t de Student :", t_stat)
print("p_value :", p_value)