import numpy as np
import scipy.special

class network:
    """=============================================ATTRIBUTE===================================="""
    """
    Knoteneigenschaften:
    inodes: First Layer, Input Nodes
    hnodes: Hidden Layer, Hidden Nodes
    onodes: Output Layer, Output Nodes
    wih: Gewichtete Input Nodes mit der ersten berechnenden Matrix
    who: Gewichtete Output Nodes mit der letzten berechnenden Matrix
    lr: Lernrate
    activation_function: Lambdafunktion oder Sigmoid 
    """
    def __init__(self,inputnodes,hiddennodes,outputnodes,learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        # Matrizen
        self.wih = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        # Einbindung der Lernrate
        self.lr = learningrate
        # Sigmoid
        self.activation_function = lambda x: scipy.special.expit(x)
        pass

        # Abschntt über das Trainieren des Netzes

    def train(self, inputs_list, targets_list):
        # Erstellen eines 2D Arrays
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T
        # Eingabe für die hidden Nodes
        hidden_inputs = np.dot(self.wih, inputs)
        # Ausgabe der Hidden Layer
        hidden_outputs = self.activation_function(hidden_inputs)
        # Eingabe für die Output Nodes
        final_inputs = np.dot(self.who, hidden_outputs)
        # Ausgabe der Output Nodes
        final_outputs = self.activation_function(final_inputs)
        #Berechnung der Fehler die das Netz gemacht hat
        output_errors = targets - final_outputs
        hidden_errors = np.dot(self.who.T, output_errors)
        # Update: Hidden und Output Layer erhalten neue Gewichtungen
        self.who += self.lr * np.dot((output_errors * final_outputs *(1.0 - final_outputs)), np.transpose(hidden_outputs))
        self.wih += self.lr * np.dot((hidden_errors * hidden_outputs *(1.0 - hidden_outputs)), np.transpose(inputs))

        pass

# Abfrage an das Neuronale Netzwerk
    def query(self, inputs_list):
        # Erstellung eines 2D Arrays
        inputs = np.array(inputs_list, ndmin=2).T
        # Berechnung des HL Inputs
        hidden_inputs = np.dot(self.wih, inputs)
        # Ausgabe der HL
        hidden_outputs = self.activation_function(hidden_inputs)
        # Eingabe in die OL
        final_inputs = np.dot(self.who, hidden_outputs)
        # Ausgabe der OL
        final_outputs = self.activation_function(final_inputs)
        return final_outputs