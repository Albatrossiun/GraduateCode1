import numpy as np
import matplotlib.pyplot as plt

def TestZGS():
    Y = [1.12, 2.04, 2.98, 3.82]
    X = Y.copy()
    index = []
    Err = []
    for i in range(100):
        index.append(i)
        Err.append([(2.49-X[0])**2,(2.49-X[1])**2,(2.49-X[2])**2,(2.49-X[3])**2])
        XX = X.copy()
        print(XX)
        X[0] = 0.15*(0.5*(XX[1]-XX[0]))+XX[0]
        X[1] = 0.15*(0.5*(XX[2]-XX[1]))+XX[1]
        X[2] = 0.15*(0.5*(XX[3]-XX[2]))+XX[2]
        X[3] = 0.15*(0.5*(XX[0]-XX[3]))+XX[3]

    plt.plot(index, Err)
    plt.show()

def TestZGS_1():
    Y = [0.6, 3.5, 7, 2, 0.1]
    X = Y.copy()
    index = []
    #Err = []
    Err_0 = []
    Err_1 = []
    Err_2 = []
    Err_3 = []
    Err_4 = []
    for i in range(100):
        index.append(i)
        Err_0.append((2.64 - X[0]) ** 2)
        Err_1.append((2.64 - X[1]) ** 2)
        Err_2.append((2.64 - X[2]) ** 2)
        Err_3.append((2.64 - X[3]) ** 2)
        Err_4.append((2.64 - X[4]) ** 2)
        #Err.append([(3.69-X[0])**2,(3.69-X[1])**2,(3.69-X[2])**2,(3.69-X[3])**2,(3.69-X[4])**2])
        XX = X.copy()
        print(XX)
        X[0] = 1.5*(0.5*(XX[1]-XX[0]))+XX[0]
        X[1] = 1.5*(0.5*((XX[2]-XX[1]) + (XX[3]-XX[1])))+XX[1]
        X[2] = 1.5*(0.5*((XX[0]-XX[2]) + (XX[1]-XX[2])))+XX[2]
        X[3] = 1.5*(0.5*(XX[4]-XX[3]))+XX[3]
        X[4] = 1.5*(0.5*(XX[2]-XX[4]))+XX[4]

    plt.plot(index, Err_0, label='sum(|x*-x0(K)|^2)')
    plt.plot(index, Err_1, label='sum(|x*-x1(K)|^2)')
    plt.plot(index, Err_2, label='sum(|x*-x2(K)|^2)')
    plt.plot(index, Err_3, label='sum(|x*-x3(K)|^2)')
    plt.plot(index, Err_4, label='sum(|x*-x4(K)|^2)')
    plt.legend(loc='upper right')
    plt.xlabel('iterations times(k)')
    plt.ylabel('Err')
    plt.show()

if __name__ == '__main__':
    TestZGS_1()