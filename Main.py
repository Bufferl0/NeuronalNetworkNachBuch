from Helper import pngWandler
from Eingabe import Eingabe
import numpy as np
# -- created by Janek Zitzmann, 17.09.2019
"""=======================================================Attribute=================================================="""
path = "C:/pythonImg/"
"""=======================================================CODE======================================================="""
#eingabe = Eingabe(path)
erg = pngWandler(path).openPictures()
np.set_printoptions(threshold=np.inf)

print(erg)
nullen = 0
einsen = 0
if erg is None:
    print("erst Bilder anlegen")
else:
    for a in erg[1]:
        if a < 1.0:
            nullen += 1
        else:
            einsen += 1
    print(nullen)
    print(einsen)

