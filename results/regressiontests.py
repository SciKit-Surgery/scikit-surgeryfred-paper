import numpy as np
from scipy import stats
from colorama import Fore, Style

def test_pvalue(slope, intercept, r_value, p_value, std_err):

    if p_value < 0.05:
        print(f"There is {Fore.RED}a significant relationship{Style.RESET_ALL}")
        print("r_value: ", r_value, "p_value: ", p_value, " Slope: ", slope)
    else:
        print(f"There is {Fore.GREEN}no significant relationship{Style.RESET_ALL}")
        print("r_value: ", r_value, "p_value: ", p_value)

def run_analysis(filename):

    array=np.loadtxt(filename, delimiter=',')

    act_tre = array[:,0]
    act_fre = array[:,1]
    exp_tre = array[:,2]
    exp_fre = array[:,3]
    exp_fle = array[:,4]
    no_fids = array[:,5]

    print("************* Running analysis for ", filename, 
                    " *****************")
    
    print("Actual TRE vs Actual FRE")
    slope, intercept, r_value, p_value, std_err = \
                    stats.linregress(act_tre, act_fre)
    test_pvalue(slope, intercept, r_value, p_value, std_err)

    print("Actual TRE vs Expected TRE")
    slope, intercept, r_value, p_value, std_err = \
                    stats.linregress(act_tre, exp_tre)
    test_pvalue(slope, intercept, r_value, p_value, std_err)

    print("Actual TRE vs Expected FRE")
    slope, intercept, r_value, p_value, std_err = \
                    stats.linregress(act_tre, exp_fre)
    test_pvalue(slope, intercept, r_value, p_value, std_err)

    print("Actual TRE vs Expected FLE")
    slope, intercept, r_value, p_value, std_err = \
                    stats.linregress(act_tre, exp_fle)
    test_pvalue(slope, intercept, r_value, p_value, std_err)


    print("Actual TRE vs No of Fiducials")
    slope, intercept, r_value, p_value, std_err = \
                    stats.linregress(act_tre, no_fids)
    test_pvalue(slope, intercept, r_value, p_value, std_err)


run_analysis('anistropic_3x.csv')
run_analysis('systematix_1.csv')
run_analysis('default.csv')
