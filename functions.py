

import numpy as np

def fed_svensson_rate(days,beta_0, beta_1,beta_2,beta_3, tau_1,tau_2):
    n = days/365
    alpha_1 = n/tau_1
    alpha_2 = n/tau_2
    factor_1 = beta_1 * (1 - np.exp(-alpha_1)) / alpha_1
    factor_2 = beta_2 * ( ((1 - np.exp(-alpha_1)) / alpha_1) - np.exp(-alpha_1))
    factor_3 = beta_3 * ( ((1 - np.exp(-alpha_2)) / alpha_2) - np.exp(-alpha_2))
    return beta_0 + factor_1 + factor_2 + factor_3
