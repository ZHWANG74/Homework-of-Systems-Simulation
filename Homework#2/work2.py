import numpy as np
from scipy.stats import rv_discrete
import matplotlib.pyplot as plt
# plt.bar(X,P,width=0.5)
# plt.xlabel("Drinking time")
# plt.ylabel("PDF for the time to drink a cup of  coffee")

x = np.linspace(0, 10, 1000)
interval1 = [1 if (i >= 3 and i <= 9) else 0 for i in x]
interval2 = [1 if (i>9) else 0 for i in x]

y = (9-x)/18*interval1

# plt.plot(x,y)
# #plt.show()
# plt.xlabel("Drinking time")
# plt.title("PDF for the time to drink a cup of  coffee")
# plt.ylabel("f(y)")
# plt.show()

# y1 = (0.5*x-1/36*x*x-1.25)*interval1+1*interval2
# plt.plot(x,y1)
# #plt.show()
# plt.xlabel("Drinking time")
# plt.ylabel("F(y)")
# plt.title("CDF for the time to drink a cup of  coffee")
# plt.show()

def generator_arrival_ivt():
    r = np.random.uniform(0,1/3)
    return 9-18*r

num_samples = 1000

# samples_ivt = [generator_arrival_ivt() for i in range(num_samples)]
# mean = np.sum(samples_ivt)/1000
# print(mean)

def calculate_sd():
    s = 0
    s1 = 0
    for i in range(1000):
        s += generator_arrival_ivt()**2
        s1 += generator_arrival_ivt()
    mean = s1 / 1000
    d = s / 1000 - mean ** 2
    sd = np.sqrt(d)
    pos_mean = mean + 1.96*(sd/np.sqrt(1000))
    neg_mean = mean - 1.96 * (sd/np.sqrt(1000))

    return sd, pos_mean, neg_mean

print(calculate_sd())



# plt.figure()
# plt.hist(samples_ivt, bins=range(2,11), color='black', label='Generated (IVT)')
# plt.xlabel('Drinking coffee Time Bin (minutes)')
# plt.ylabel('Count')
# plt.title('Histogram for Drinking coffee time ($n$={})'.format(num_samples))
# plt.legend()
# plt.show()