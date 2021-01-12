import csv
import scipy.stats
import numpy as np
import matplotlib.pyplot as plt

categories = []
scores = []
with open("all_logs.log", mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        timestamp = row[0]
        if timestamp == '2020-07-08 18:45:17':
            print ("Skipping " , timestamp, "there were 22 entries in this log")
            continue 
        if timestamp == '2020-07-08 18:45:43':
            print ("Skipping " , timestamp, "there were 22 entries in this log")
            continue

        categories.append(row[2])
        scores.append(row[3])

scores
actual_tre = []
expected_tre = []
expected_fre = []
expected_fle = []
actual_fre = []

for index, cat in enumerate(categories):
    if 'Actual TRE' in cat:
        actual_tre.append(scores[index])
    if 'FLE and Number of Fids' in cat:
        expected_fle.append(scores[index])
    if 'Expected TRE' in cat:
        expected_tre.append(scores[index])
    if 'Expected FRE' in cat:
        expected_fre.append(scores[index])
    if 'Actual FRE' in cat:
        actual_fre.append(scores[index])

assert len(actual_tre) == len(expected_tre) == len(expected_fre) == len(expected_fle) == len(actual_fre)

def mean_and_fail_rate(scores):
    array = np.array(scores, dtype=np.float64)
    mean = np.mean(array)
    fails = np.count_nonzero(array < 0)
    fail_rate = float(fails) / float (len(scores))
    return mean, fail_rate

names=["Overall", "Actual TRE", "Actual FRE", "Expected FLE", "Expected FRE", "Expected TRE"]
means=[]
fail_rates=[]

mean, fail_rate = mean_and_fail_rate(scores)
means.append(mean)
fail_rates.append(fail_rate)

mean, fail_rate = mean_and_fail_rate(actual_tre)
means.append(mean)
fail_rates.append(fail_rate)

mean, fail_rate = mean_and_fail_rate(actual_fre)
means.append(mean)
fail_rates.append(fail_rate)

mean, fail_rate = mean_and_fail_rate(expected_fle)
means.append(mean)
fail_rates.append(fail_rate)

mean, fail_rate = mean_and_fail_rate(expected_fre)
means.append(mean)
fail_rates.append(fail_rate)

mean, fail_rate = mean_and_fail_rate(expected_tre)
means.append(mean)
fail_rates.append(fail_rate)

for index, name in enumerate(names):
    print(name, " (mean, fail rate): ", means[index], fail_rates[index])

reps=6 # hack to test stat power

t_stat, p_value = scipy.stats.ttest_ind(np.array(actual_tre, dtype=np.float64).repeat(reps),
                                        np.array(scores, dtype=np.float64).repeat(reps), 
                                        equal_var = False, nan_policy='raise')
print ("T Test actual TRE vs all", t_stat, p_value)
t_stat, p_value = scipy.stats.ttest_ind(np.array(actual_fre, dtype=np.float64).repeat(reps),
                                        np.array(scores, dtype=np.float64).repeat(reps), 
                                        equal_var = False, nan_policy='raise')
print ("T Test actual FRE vs all", t_stat, p_value)
t_stat, p_value = scipy.stats.ttest_ind(np.array(expected_fle, dtype=np.float64).repeat(reps),
                                        np.array(scores, dtype=np.float64).repeat(reps), 
                                        equal_var = False, nan_policy='raise')
print ("T Test expected FLE vs all", t_stat, p_value)

t_stat, p_value = scipy.stats.ttest_ind(np.array(expected_fre, dtype=np.float64).repeat(reps),
                                        np.array(scores, dtype=np.float64).repeat(reps), 
                                        equal_var = False, nan_policy='raise')
print ("T Test expected FRE vs all", t_stat, p_value)

t_stat, p_value = scipy.stats.ttest_ind(np.array(expected_tre, dtype=np.float64).repeat(reps),
                                        np.array(scores, dtype=np.float64).repeat(reps), 
                                        equal_var = False, nan_policy='raise')
print ("T Test expected TRE vs all", t_stat, p_value)

t_stat, p_value = scipy.stats.ttest_ind(np.array(actual_tre, dtype=np.float64).repeat(reps), 
                                        np.array(actual_fre, dtype=np.float64).repeat(reps),
                                        equal_var = True, nan_policy='raise')
print ("T Test actual TRE vs actual FRE", t_stat, p_value)

fig, ax1 = plt.subplots()
fontsize=26
ticksize=14
plt.setp(ax1.get_xticklabels(), rotation='horizontal', fontsize=ticksize)
plt.setp(ax1.get_yticklabels(), rotation='horizontal', fontsize=ticksize)
ax1.bar(names, means, width=0.5, label='Mean Scores')
ax1.set_ylabel('Mean Score', fontsize=fontsize )
ax1.set_xlabel('Statistic Shown', fontsize=fontsize)

ax2 = ax1.twinx()
plt.setp(ax2.get_yticklabels(), rotation='horizontal', fontsize=ticksize)
ax2.set_ylabel('Failure Rate', fontsize=fontsize)
ax2.plot(names, fail_rates, marker='o', linestyle='none', color='black', markersize=12, label='Under Treatment Rate')

fig.legend( fontsize=fontsize )
plt.show()
