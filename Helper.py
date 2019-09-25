import matplotlib.pyplot
import numpy as np
import os

# --Created by Janek Zitzmann, 17.09.2019
class pngWandler:
    def __init__(self, path):
        self.path = path

    def openPictures(self):
        """gibt ein array aus paaren zurück, alle ungeraden zahlen sind die Lösung zur darauffolgenden Matrix"""
        erg = []  # ergebnis array aus tupeln initialisiert
        try:
            files = os.listdir(self.path)
        except FileNotFoundError:
            os.makedirs(self.path)
        "iteriere über alle files im gegebenen Ordner"
        for filename in os.listdir(self.path):  # listet die name aller gefundenen dateien im gefundenen ordner auf
            "lies matrix ein"
            picturematrix = matplotlib.pyplot.imread(self.path + filename)
            "Speichere Ergebnis ab"
            richtigeantwort = filename[0]  # per konvention ist das erste Zeichen des filenames das richtige Ergebnis
            "matrix transformieren"
            picturematrix = self.eindimensionalegrauwertmatrix(picturematrix)
            "Paar im Array abspeichern"
            tupel = (richtigeantwort, picturematrix)
            erg += tupel
            return erg

    @staticmethod
    def eindimensionalegrauwertmatrix(matrix):
        """macht die matrix flach und ersetzt RGB-Pixel durch den R Wert """
        ergebnis = []
        i = 0
        j = 0
        for zeile in matrix:
            for spalte in zeile:
                "Der erste Wert wird für den ganzen Pixel genommen, da RGB bei schwarz-weiß gleich ausgeprägt"
                ergebnis.append(spalte[0])
        return ergebnis
