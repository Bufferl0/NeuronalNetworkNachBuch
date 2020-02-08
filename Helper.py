from uu import Error

import matplotlib.pyplot
import numpy as np
import numpy
import os
import shutil
from Network import network

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
    right = 0
    wrong = 0
    index = 1
    while index < len(pictures):
        result = network.query(pictures[index])
        formattedresult = getIndexOfMaxValue(result)
        if formattedresult == getIndexOfMaxValue(pictures[index-1]):
            right += 1
        else:
            wrong += 1
        index += 2
    return right, wrong

def readFromMnist():
    input_nodes = 784
    hidden_nodes = 300
    output_nodes = 10
    learning_rate = 0.2

    n = network(input_nodes, hidden_nodes, output_nodes, learning_rate)

    # load the mnist training data csv file into a list
    training_data_file = open("mnist_dataset/mnist_train_100.csv", "r")
    training_data_list = training_data_file.readlines()
    training_data_file.close()

    # train the neuronal network

    # epochs is the number of times the training data set is used for training
    epochs = 5

    for e in range(epochs):
        # go through all records in the training data set
        for record in training_data_list:
            # split the record by the ',' commas
            all_values = record.split(',')
            # scale and shift the inputs
            inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
            # create the target output values (all 0.01, except the desired label which is 0.99)
            targets = numpy.zeros(output_nodes) + 0.01
            # all_values[0] is the target label for this record
            targets[int(all_values[0])] = 0.99
            n.train(inputs, targets)
            pass
        pass

    # load the mnist test data CSV file into a list
    test_data_file = open("mnist_dataset/mnist_test_10.csv", 'r')
    test_data_list = test_data_file.readlines()
    test_data_file.close()

    # test the neural network

    # scorecard for how well the network performs, initially empty
    scorecard = []

    # go through all the records in the test data set
    for record in test_data_list:
        # split the record by the ',' commas
        all_values = record.split(',')
        # correct answer is first value
        correct_label = int(all_values[0])
        # scale and shift the inputs
        inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        # query the network
        outputs = n.query(inputs)
        # the index of the highest value corresponds to the label
        label = numpy.argmax(outputs)
        # append correct or incorrect to list
        if label == correct_label:
            # network's answer matches correct answer, add 1 to scorecard
            scorecard.append(1)
        else:
            # network's answer doesn't match correct answer, add 0 to scorecard
            scorecard.append(0)
            pass

        pass

    # calculate the performance score, the fraction of correct answers
    scorecard_array = numpy.asarray(scorecard)
    print(scorecard)
    print("performance = ", scorecard_array.sum() / scorecard_array.size)
