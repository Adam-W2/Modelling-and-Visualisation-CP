import matplotlib
matplotlib.use("TKAgg")
import numpy as np
import random
import matplotlib.pyplot as plt

"""""
This file contains all the functions for updating the spins (Glauber and Kawasaki) as
well as the function that take measurements and calculate errors.
"""""

def Kawasaki(X,Y,kT,spins):
    #loop over whole array
    for i in range(X):
        for j in range(Y):
            #pick two random points
            itrial1 = np.random.randint(0,X)
            jtrial1 = np.random.randint(0,Y)
            itrial2 = np.random.randint(0,X)
            jtrial2 = np.random.randint(0,Y)

            spin1 = spins[itrial1][jtrial1]
            spin2 = spins[itrial2][jtrial2]

            #check if the two points aren't the same point
            if spin1 != spin2:
                #flip spins
                spin1 = -1 * spin1
                spin2 = -1 * spin2
                diffx = itrial1 - itrial2
                diffy = jtrial1 - jtrial2

                #Calculate the energy change for the new spins
                Edelta1 = -2 * spin1 * (spins[(itrial1 + 1) % X][jtrial1] + spins[(itrial1 - 1) % X][jtrial1] +
                                        spins[itrial1][(jtrial1 + 1) % X] + spins[itrial1][(jtrial1 - 1) % X])

                Edelta2 = -2 * spin2 * (spins[(itrial2 + 1) % X][jtrial2] + spins[(itrial2 - 1) % X][jtrial2] +
                                        spins[itrial2][(jtrial2 + 1) % X] + spins[itrial2][(jtrial2 - 1) % X])

                Edelta = Edelta1 + Edelta2
                #Calculate the absolute distance between the two points
                distance = np.sqrt(min([diffx,X - diffx]) ** 2 + min([diffy,Y - diffy]) ** 2)

                #If the absolute distance is 1, account for over counting
                if distance == 1:
                    Edelta += 4

                #Apply metropilis algorithm
                r = random.random()
                if r <= np.exp(-Edelta / kT):
                    spins[itrial1,jtrial1] = spin1
                    spins[itrial2,jtrial2] = spin2


def Glauber(X,Y,kT,spins):
    #Loop over whole array
    for i in range(X):
        for j in range(Y):
            #Pick random point
            itrial = np.random.randint(0,X)
            jtrial = np.random.randint(0,Y)

            #Flip point spin
            spin_new = -spins[itrial,jtrial]

            #Calculate the energy difference
            Edelta = -2 * spin_new * (spins[(itrial + 1) % X][jtrial] + spins[(itrial - 1) % X][jtrial] +
                                      spins[itrial][(jtrial + 1) % X] + spins[itrial][(jtrial - 1) % X])

            #Apply metropolis algorithm
            r = random.random()
            if r <= np.exp(-Edelta / kT):
                spins[itrial,jtrial] = spin_new


def measure(X,Y,spins):
    E = 0
    M = 0
    #Loop over entire array
    for i in range(X):
        for j in range(Y):

            #Calculate the energy and magnetisation for whole array
            E += -1/2 * spins[i][j] * (spins[(i + 1) % X][j] + spins[(i - 1) % X][j] + spins[i][(j + 1) % X] +
                                     spins[i][(j - 1) % X])
            M += spins[i][j]

    return E,M


def calc_c(X,kT,E,E2):
    #Calculate the specific heat capacity
    c = (E2-np.power(E,2))/(np.power(X,2) * np.power(kT,2))
    return c

def calc_x(X,kT,M,M2):
    #Calcualte the susepectibility
    x = (M2-np.power(M,2))/(np.power(X,2) * kT)
    return x

def bootstrap(L,func,X,kT):

    masterlist = []

    #Set number of k sets you want to resample
    for n in range(1000):
        sidelist1 = []
        sidelist2 = []

        #Loop over length of input list and extract random values, appending to list
        for i in range(len(L)):
            val = L[np.random.randint(0,len(L))]

            #Calculate the squared version and append
            val2 = val ** 2

            sidelist1.append(val)
            sidelist2.append(val2)

        #Calcute averages for both lists
        A = sum(sidelist1)/len(sidelist1)
        B = sum(sidelist2)/len(sidelist2)
        masterlist.append(func(X,kT,A,B))

    #Create squared list and calulate averages for specific heat
    masterlist2 = [n**2 for n in masterlist]
    c = sum(masterlist)/len(masterlist)
    c2 = sum(masterlist2)/len(masterlist2)

    #Calculate error
    error = np.sqrt(c2-c**2)
    return error

def jacknife(L,func,X,kT):
    n = len(L)
    jacknife_estimate = np.zeros(n)

    #Loop over length of input list
    for i in range(n):
        #Create new list and remove ith component
        sample = np.delete(L,i)
        #m.remove(L[i])

        #Create squared version list and calculate specific heat, appending to masterlist
        #m2 = [n ** 2 for n in m]
        sample2 = np.square(sample)

        #A = sum(m)/len(m)
        #B = sum(m2)/len(m2)

        samplemean = sample.mean()
        sample2mean = sample2.mean()
        jacknife_estimate[i] = func(X,kT,samplemean,sample2mean)

    #Create squared specific heat list and calcuate averages
    jacknife_estimate2 = np.square(jacknife_estimate)
    c = jacknife_estimate.mean()
    c2 = jacknife_estimate2.mean()

    #Calculate errors
    error = np.sqrt(c2-c**2) * np.sqrt(len(L))
    return error
def run_dynamics(nsteps,X,D,kT,spins):
    """""
    Large function that takes in all previous functions to run the simulation as well
    as take measurements and calculate all the errors. There is also animation options
    but right now these only work by commenting it in or out with no user input from console
    
    nsteps = number of sweeps done
    X = dimensions of array
    D = dynamic to use, either G for Glauber or K for Kawasaki
    kT = Temperature in Kelvin
    spins = array of intilised spins, numpy array 
    """""

    Y = X
    if D == "G":
        #Create masterlists for each measurement
        Elist = []
        Mlist = []
        E2list = []
        modMlist = []
        M2list = []

        #Loop over number of desired sweeps updating the spins each sweep
        for n in range(nsteps):
            #Apply Glauber dynamics to update spins
            Glauber(X,Y,kT,spins)
            #After 100 sweeps measurements are started to be taken. Every 10 sweeps it takes measurements
            if n % 10 == 0 and n > 100:
                #Appends values to each list
                E,M = measure(X,Y,spins)
                Elist.append(E)
                E2list.append(E**2)
                Mlist.append(M)
                modMlist.append(np.absolute(M))
                M2list.append(M**2)

        #Calulates an average for each measurement list
        avE = sum(Elist)/len(Elist)
        avE2 = sum(E2list)/len(E2list)
        avM = sum(Mlist)/len(Mlist)
        avmodM = sum(modMlist)/len(modMlist)
        avM2 = sum(M2list)/len(M2list)

        #Calculates the specific heat and suseptibility
        c = calc_c(X,kT,avE,avE2)
        x = calc_x(X,kT,avM,avM2)

        #Calculates the erorr
        error_c_boot = bootstrap(Elist,calc_c,X,kT)
        error_m_boot = bootstrap(Mlist,calc_x,X,kT)
        error_c_jack = jacknife(Elist,calc_c,X,kT)
        error_m_jack = jacknife(Mlist,calc_x,X,kT)

        return [avE,avM,avmodM,c,x,error_c_boot,error_c_jack,error_m_boot,error_m_jack],spins

    elif D == "K":
        Elist = []
        E2list = []

        #Loops through number of desired sweeps
        for n in range(nsteps):
            #Update spins using Kawasaki dynamics
            Kawasaki(X,Y,kT,spins)
            #After 100 sweeps measurements are started to be taken. Every 10 sweeps it takes measurements
            if n % 10 == 0 and n > 100:
                E,M = measure(X,Y,spins)
                Elist.append(E)
                E2list.append(E**2)

        #Calculates averages for each value list
        avE = sum(Elist) / len(Elist)
        avE2 = sum(E2list) / len(E2list)

        #Calculates specific heat
        c = calc_c(X,kT,avE,avE2)

        #Calculates the error using Jacknife or Bootstrap
        error_c_boot = bootstrap(Elist,calc_c,X,kT)
        error_c_jack = jacknife(Elist,calc_c,X,kT)

        return [avE,c,error_c_boot,error_c_jack], spins

    else:
        print("Incorrect dynamics given, check your spelling?")