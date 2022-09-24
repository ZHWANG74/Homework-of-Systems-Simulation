import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

_lambda = 2
z = np.linspace(0,10)
pdf = _lambda*np.exp(-_lambda*z)
def generator_arrival_ivt():
    r = np.random.rand()
    return -np.log(1-r)/_lambda

for i in range(0,10):
    print("first 10 z: {:.2f} min".format(generator_arrival_ivt()))

num_samples = 1000

samples_ivt = [generator_arrival_ivt() for i in range(num_samples)]

def sum_times():
    times = 0
    for i in range(num_samples):
        if i < 10:
            times += generator_arrival_ivt()
            print(times)
        else:
            times += generator_arrival_ivt()
    return times

print(sum_times())

def people_nums_min():
    sum_time = 0
    j = 0
    A = [0]*300
    for i in range(num_samples):
        sum_time += generator_arrival_ivt()
        if sum_time < 300:
            if sum_time - (j+1) < 0:
                A[j] += 1
            else:
                j += 1
    return A
s = people_nums_min()
print(s)
print(np.sum(s))

plt.figure()
plt.hist(samples_ivt, bins=range(10), color='black', label='Generated (IVT)')
plt.plot(z, pdf*num_samples, '-b', label='Theoretical')
plt.xlabel('Inter-arrival Time Bin (minutes)')
plt.ylabel('Count')
plt.title('Histogram for Inter-arrival Time Samples ($n$={})'.format(num_samples))
plt.legend()
plt.show()

plt.figure()
plt.hist(s, bins= range(8), color='black', label='the number of customers')
plt.xlabel('the number of customers arriving')
plt.ylabel('Count')
plt.title('Histogram for Inter-arrival Time Samples ($n$={})'.format(num_samples))
plt.legend()
plt.show()