# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
X=np.array([1, 2, 3, 4, 5, 6])
P=np.array([1/36, 1/12, 5/36, 7/36, 1/4, 11/36])
#Ex = mydist.expect()
#print(Ex)

def generate_demand_ivt():
    """Generates a demand following the inverse transform method.

    Returns:
        demand (int): the size of coffee demanded
    """
    # generate a random sample r
    r = np.random.rand()

    # check the first cdf entry (index 0)
    if r <= y1[0]:
        return X[0]
    # check the second cdf entry (index 1)
    elif r <= y1[1]:
        return X[1]
    # check the third cdf entry (index 2)
    elif r <= y1[2]:
        return X[2]
    # otherwise no need to check, it's the final CDF entry (index 3)
    elif r <= y1[3]:
        return X[3]
    # check the third cdf entry (index 2)
    elif r <= y1[4]:
        return X[4]
    else:
        return X[5]


import matplotlib.pyplot as plt
# plt.bar(X,P,width=0.5)
# plt.xlabel("random variable X")
# plt.ylabel("p(x)")
# plt.title("PMF for the maximum value of two six-sided dice.")
# plt.show()

y1 = np.array([1/36,1/9,1/4,4/9,25/36,1])
# plt.step(X, y1)
# plt.xlabel("random variable X")
# plt.ylabel("F(x)")
# plt.title("CDF for the maximum value of two six-sided dice.")
# plt.show()


num_samples = 1000
samples_ivt = [generate_demand_ivt() for i in range(num_samples)]

mean = np.sum(samples_ivt)/1000
print(mean)
def calculate_sd():
    s = 0
    s1 = 0
    for i in range(1000):
        s += generate_demand_ivt()**2
        s1 += generate_demand_ivt()
    mean1 = s1/1000
    d = s/1000-mean**2
    sd = np.sqrt(d)
    return sd

print(calculate_sd())



# plt.figure()
# plt.hist(samples_ivt, bins=range(1,7), color='black', label='Generated (IVT)')
# plt.xlabel('the maximum value of two six-sided dice')
# plt.ylabel('Count')
# plt.title('Histogram for Samples ($n$={})'.format(num_samples))
# plt.legend()
# plt.show()

# import math
# interval = 1.96*1.415/math.sqrt(1000)
