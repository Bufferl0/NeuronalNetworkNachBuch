from Helper import pngWandler
from Eingabe import Eingabe
import numpy as np
# -- created by Janek Zitzmann, 17.09.2019
"""=======================================================Attribute=================================================="""
path = "C:/pythonImg/"
"""=======================================================CODE======================================================="""
#eingabe = Eingabe(path)
erg = pngWandler(path).openPictures()
np.set_printoptions(threshold=np.inf) # wird für Ausgabe der Matrizen benötigt
eing = Eingabe(path)


