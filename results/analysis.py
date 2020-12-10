import numpy as np
from scipy import stats
from colorama import Fore, Style


def run_analysis(filename):

    array=np.loadtxt(filename, delimiter=',')

    act_tre = array[:,0]
    act_fre = array[:,1]
    exp_tre = array[:,2]
    exp_fre = array[:,3]
    exp_fle = array[:,4]
    no_fids = array[:,5]

    print("Running analysis for ", filename)
    
    print("Actual TRE vs Actual FRE")
    slope, intercept, r_value, p_value, std_err = \
                    stats.linregress(act_tre, act_fre)
    if p_value < 0.05:
        print(f"There is {Fore.RED}a significant relationship{Style.RESET_ALL}")
        print("r_value: ", r_value, "p_value: ", p_value)
    else:
        print(f"There is {Fore.GREEN}no significant relationship{Style.RESET_ALL}")
        print("r_value: ", r_value, "p_value: ", p_value)

    print("Actual TRE vs Expected TRE")
    slope, intercept, r_value, p_value, std_err = \
                    stats.linregress(act_tre, exp_tre)
    if p_value < 0.05:
        print(f"There is {Fore.RED}a significant relationship{Style.RESET_ALL}")
        print("r_value: ", r_value, "p_value: ", p_value)
    else:
        print(f"There is {Fore.GREEN}no significant relationship{Style.RESET_ALL}")
        print("r_value: ", r_value, "p_value: ", p_value)

    print("Actual TRE vs Expected FRE")
    slope, intercept, r_value, p_value, std_err = \
                    stats.linregress(act_tre, exp_fre)
    if p_value < 0.05:
        print(f"There is {Fore.RED}a significant relationship{Style.RESET_ALL}")
        print("r_value: ", r_value, "p_value: ", p_value)
    else:
        print(f"There is {Fore.GREEN}no significant relationship{Style.RESET_ALL}")
        print("r_value: ", r_value, "p_value: ", p_value)

    print("Actual TRE vs Expected FLE")
    slope, intercept, r_value, p_value, std_err = \
                    stats.linregress(act_tre, exp_fle)
    if p_value < 0.05:
        print(f"There is {Fore.RED}a significant relationship{Style.RESET_ALL}")
        print("r_value: ", r_value, "p_value: ", p_value)
    else:
        print(f"There is {Fore.GREEN}no significant relationship{Style.RESET_ALL}")
        print("r_value: ", r_value, "p_value: ", p_value)


    print("Actual TRE vs No of Fiducials")
    slope, intercept, r_value, p_value, std_err = \
                    stats.linregress(act_tre, no_fids)
    if p_value < 0.05:
        print(f"There is {Fore.RED}a significant relationship{Style.RESET_ALL}")
        print("r_value: ", r_value, "p_value: ", p_value)
    else:
        print(f"There is {Fore.GREEN}no significant relationship{Style.RESET_ALL}")
        print("r_value: ", r_value, "p_value: ", p_value)


run_analysis('anistropic_3x.csv')
run_analysis('systematix_1.csv')

