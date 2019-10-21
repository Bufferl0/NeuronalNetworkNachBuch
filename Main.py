from Helper import pngWandler
from Eingabe import Eingabe
import numpy as np
from Network import network
# -- created by Janek Zitzmann, 17.09.2019
"""=======================================================Attribute=================================================="""
path = "C:/pythonImg/"
inputnodes = 784
"""=======================================================CODE======================================================="""
def transformAnswer(antwortMatrix):
    index = np.where(antwortMatrix == np.amax(antwortMatrix))
    return index

np.set_printoptions(threshold=np.inf) # wird für Ausgabe der Matrizen benötigt
eingabe = Eingabe(path)
erg = pngWandler(path).openPictures()
print(erg[1])
images = []
targets = []
i = 0
j = 0
nw = network(inputnodes, 300, 10, 0.4)
while j < 1:
    for obj in erg:
        if i+1 < len(erg):
            nw.train(erg[i+1], erg[i])
        i += 2
    j += 1

print(transformAnswer(nw.query(erg[3])))
print(transformAnswer(nw.query(erg[3])))
print(transformAnswer(nw.query(erg[7])))
print(transformAnswer(nw.query(erg[7])))
print(transformAnswer(nw.query(erg[13])))









