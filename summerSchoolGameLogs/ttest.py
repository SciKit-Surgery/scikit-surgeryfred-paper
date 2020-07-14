#! /home/thompson/data/FiducialRegistrationEducationalDemonstration/.tox/py37/bin/python
import csv
import scipy.stats
import numpy as np

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


print ("read ", len(categories), " entries.")
t_stat, p_value = scipy.stats.ttest_ind(np.array(actual_tre, dtype=np.float64),
                                        np.array(scores, dtype=np.float64), 
                                        equal_var = False, nan_policy='raise')
print ("T Test actual TRE vs all", t_stat, p_value)
t_stat, p_value = scipy.stats.ttest_ind(np.array(actual_fre, dtype=np.float64),
                                        np.array(scores, dtype=np.float64), 
                                        equal_var = False, nan_policy='raise')
print ("T Test actual FRE vs all", t_stat, p_value)
t_stat, p_value = scipy.stats.ttest_ind(np.array(expected_fle, dtype=np.float64),
                                        np.array(scores, dtype=np.float64), 
                                        equal_var = False, nan_policy='raise')
print ("T Test expected FLE vs all", t_stat, p_value)

t_stat, p_value = scipy.stats.ttest_ind(np.array(expected_fre, dtype=np.float64),
                                        np.array(scores, dtype=np.float64), 
                                        equal_var = False, nan_policy='raise')
print ("T Test expected FRE vs all", t_stat, p_value)

t_stat, p_value = scipy.stats.ttest_ind(np.array(expected_tre, dtype=np.float64),
                                        np.array(scores, dtype=np.float64), 
                                        equal_var = False, nan_policy='raise')
print ("T Test expected TRE vs all", t_stat, p_value)

t_stat, p_value = scipy.stats.ttest_ind(np.array(actual_tre, dtype=np.float64), 
                                        np.array(actual_fre, dtype=np.float64),
                                        equal_var = True, nan_policy='raise')
print ("T Test actual TRE vs actual FRE", t_stat, p_value)
