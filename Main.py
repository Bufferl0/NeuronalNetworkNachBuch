# Import
from Helper import pngWandler
import Helper
from Eingabe import Eingabe
import numpy as np
from Network import network
# -- created by Janek Zitzmann, 17.09.2019
# -- comments added by Pascal Kattler, 12.02.2020
# -- comments added by Pascal Kattler, 13.02.2020

"""=======================================================Attribute=================================================="""
# Es werden zwei Paths benötigt da das Programm aus zwei Quellen lernen kann.
path = "C:/pythonImgTrain/"  # Datenbankimages
path2 = "C:/pythonImg/"      # Speicherort der Eingabe des Benutzers

# Zu Beginn müssen die Input Nodes festgelegt werden
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
nw = network(inputnodes, 300, 10, 0.3)
while j < 3:
    for obj in erg:
        if i+1 < len(erg):
            nw.train(erg[i+1], erg[i])
        i += 2
    j += 1
eingabe = Eingabe(path, nw)
right, wrong = Helper.testNetwork(nw, path)
print(right)
print(wrong)
Helper.readFromMnist()









