from Helper import pngWandler
import Helper
from Eingabe import Eingabe
import numpy as np
from Network import network
# -- created by Janek Zitzmann, 17.09.2019
"""=======================================================Attribute=================================================="""
path = "C:/pythonImg/"
inputnodes = 784
"""=======================================================CODE======================================================="""
def transformAnswer(antwortMatrix):
    index = Helper.getIndexOfMaxValue(antwortMatrix)
    return index

np.set_printoptions(threshold=np.inf) # wird für Ausgabe der Matrizen benötigt

erg = pngWandler(path).openPictures()
images = []
targets = []
i = 0
j = 0
nw = network(inputnodes, 300, 10, 0.6)
while j < 1:
    for obj in erg:
        if i+1 < len(erg):
            nw.train(erg[i+1], erg[i])
        i += 2
    j += 1
eingabe = Eingabe(path, nw)
print(transformAnswer(nw.query(erg[3])))
print(transformAnswer(nw.query(erg[5])))
print(transformAnswer(nw.query(erg[13])))









