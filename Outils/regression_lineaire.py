# -*- coding: utf-8 -*-

"""
Code Python de tracé et le calcul de régression linaire
Développé par Th. G, ENS de Lyon, le 13/04/2019.
"""

from pylab import *
from scipy import *
from numpy import *
import matplotlib.pyplot as plt
from scipy import stats


A=open("test.csv", 'r')
A.readline()
X=array([])
Y=array([])
for i in A:
    var=i.split(",")
    x=float(var[0])
    y=float(var[1])
    X=append(X,x)
    Y=append(Y,y)
    
    errX = 0.1
    errY = 0.1
    
slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)
r2 = r_value*r_value
print("Résultats de la régression :")
print("a=",slope) 
print("b=",intercept)
print("r2=",r2)

fig, ax = plt.subplots(1) 

errorbar(X, Y, errY, errX, 'o', label='Points expérimentaux')
plt.plot(X, intercept + slope*X, 'r', label='Régression linéaire')

plt.legend()

xlabel('Variable X')
ylabel('Variable Y')
title('Tracé de la régression linéaire')
grid(True)

plt.show()
