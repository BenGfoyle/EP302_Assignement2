"""
@author: Ben Guilfoyle - github.com/bengfoyle
@Overview: Script to calculate vibrational and rotational energy of ground HBr
"""

import matplotlib.pyplot as plt
from numpy import sqrt
from scipy import constants as con

#constants
PI = con.pi()
FVIB = 7.68e13 #known experiemntally
HBAR = con.hbar
H = con.Planck


def getERot(j):
	"""Calculate Rotational energy from known formula"""
	ERot = (j * (j +1)) * ((HBAR**2) / (2 * I))
	return ERot
	
def getEVib(v):
	"""Calculate Vibrational energy from known formula"""
	EVib = (v + 0.5) * H * FVIB	
	return EVib

def makePlot(xAxis,yAxis):
	plt.plot(xAxis,yAxis)
	plt.xlabel("Energy eV")
	plt.ylabel("Absorbtion")
	plt.grid()
	plt.show()
	
ETot = []
level = [1,2,3,4,5,6]
for i in range(0,1):
	EVib = getEVib(i)
	for j in range(0,5):
		ERot = getERot(j)
		ETot.append(Erot + EVib)

makePlot(Etot[0,5],level)
makePlot(Etot[6,11],level)