import numpy as np
from scipy import stats
from colorama import Fore, Style


def compare_means(filename1, filename2):

    array1=np.loadtxt(filename1, delimiter=',')
    array2=np.loadtxt(filename2, delimiter=',')

    for i in range(6):
        print ("Testing col ", i)
        print(stats.ks_2samp(array1[:,i], array2[:,i]))
        print("mean 1: ", np.mean(array1[:,i]))
        print("mean 2: ", np.mean(array2[:,i]))


compare_means('default.csv', 'anistropic_3x.csv')
compare_means('default.csv', 'systematix_1.csv')
