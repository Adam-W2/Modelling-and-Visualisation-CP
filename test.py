import matplotlib.pyplot as plt
import numpy as np
import random

X1 = 50
kT1 = 1
def bootstrap(L,func,X,kT):
    masterlist = []

    for n in range(1000):
        sidelist1 = []
        sidelist2 = []

        for i in range(len(L)):
            val = L[np.random.randint(0,len(L))]
            val2 = val ** 2
            sidelist1.append(val)
            sidelist2.append(val2)

        A = sum(sidelist1)/len(sidelist1)
        B = sum(sidelist2)/len(sidelist2)
        masterlist.append(func(X,kT,A,B))

    masterlist2 = [n**2 for n in masterlist]
    c = sum(masterlist)/len(masterlist)
    c2 = sum(masterlist2)/len(masterlist2)

    error = np.sqrt(c2-c**2)
    return error

def calc_c(X,kT,E,E2):
    c = (E2-np.power(E,2))/(np.power(X,2) * np.power(kT,2))
    return c


avE = [5,6,5,4,7,6,5,5,4]
error_c_boot = bootstrap(avE,calc_c,X1,kT1)
print(error_c_boot)