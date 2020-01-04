from uu import Error

import matplotlib.pyplot
import numpy as np
import os
import shutil

# --Created by Janek Zitzmann, 17.09.2019
class pngWandler:
    """Öfnet alle Bilder im angegeben Pfad und wandelt sie in ein 1D Array um"""
    """===========================ATTRIBUTE===================================="""
    "path -> save path image directory"
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
            if filename != "currentImgCount.txt":
                "lies matrix ein"

                picturematrix = matplotlib.pyplot.imread(self.path + filename)
                picturematrix = picturematrix.flatten()
                scaled_matrix = (np.asfarray(picturematrix[0:]) - 1) * -1 + 0.01
                "Speichere Ergebnis ab"
                richtigeantwort = filename[0]  # per konvention ist das erste Zeichen des filenames das richtige Ergebnis
                "matrix transformieren"
                #picturematrix = self.eindimensionalegrauwertmatrix(picturematrix)
                "Paar im Array abspeichern"
                richtigeantwortAlsMatrix = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                richtigeantwortAlsMatrix[int(richtigeantwort)] = 0.99
                #tupel = (richtigeantwortAlsMatrix, picturematrix)
                tupel = (richtigeantwortAlsMatrix, scaled_matrix)
                erg += tupel
        return erg

    @staticmethod
    def eindimensionalegrauwertmatrix(matrix):
        """macht die matrix flach und ersetzt RGB-Pixel durch den R Wert """
        ergebnis = np.empty(784)
        for zeile in matrix:
            for spalte in zeile:
                np.append(ergebnis, spalte)



        '''print("================================================")
        print(ergebnis)
        file = open("C:/pythonImg/" + "Matrix.txt", "w")
        file.write(str(ergebnis))
        file.write("=================================================")
        file.write("\n")
        '''
        return ergebnis

def deleteFilesInFolder(path):
    folder = path
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def getIndexOfMaxValue (array):
    maxIndex = 0
    currentIndex = 1
    maxValue = array[0]
    while currentIndex < len(array):
        if array[currentIndex] > maxValue:
            maxValue = array[currentIndex]
            maxIndex = currentIndex
        currentIndex += 1
    return maxIndex

def testNetwork(network, pathOfTestDatabase):
    wandler = pngWandler(pathOfTestDatabase)
    pictures = wandler.openPictures()
    index = 1
    while index < len(pictures):

        index += 2
