from tkinter import *
import PIL
from PIL import Image, ImageDraw
import Helper
from Helper import pngWandler
from Network import network
import os,shutil

# --Created by Janek Zitzmann, 18.09.2019
class Eingabe:
    #TODO Attribute auflisten
    """========================ATTRIBUTE========================="""
    """
    Bildeigenschaften:
    size: Größe des Bildes
    savepath: Speicherort, bzw der Weg dorthin 
    current_save_number: Abgespeicherte Bilder
    image1: Aktuelles Bild, welcher durch den Benutzer erstellt wird
    
    Programmspezifisch:
    draw: Zeichenmethode 
   
   Knöpfe:
   btn_save: Bild wird gespeichert
    btn_clear: Zeichenfläche wird gecleared 
    text_box: Antwortfeld für die einzige richtige Antwort
    
    """

    def __init__(self, savepath, neuronal_network):
        self.size = (28, 28)
        self.savepath = savepath
        file = open(self.savepath + "currentImgCount.txt", "w+") #TODO evtl. Fehler beim öffnen -> FIle wird neu angelegt
        self.current_save_number = file.read()
        "falls das file leer ist wird 0 als filename angesetzt und in das file geschrieben"
        if not self.current_save_number: # empty strings are considered false in boolean
            self.current_save_number = "0"
            file.write(str(self.current_save_number))
        file.close()
        self.network = neuronal_network


        self.root = Tk()
        self.cv = Canvas(self.root, width=200, height=200, bg='white')
        self.image1 = PIL.Image.new('L', (200, 200), "white") #1 = mode, 1-bit Schwarz-Weiß
        self.draw = ImageDraw.Draw(self.image1)
        self.cv.bind('<B1-Motion>', self.paint)
        self.cv.pack(expand=YES, fill=BOTH)
        self.text_box = Text(self.root, height=2, width=4)
        self.label_query_answer = Label(self.root, text="ausgabe")
        "Button_init"
        self.btn_save = Button(text="save", command=self.save)
        self.btn_clear = Button(text="Clear", command=self.clear)
        self.btn_query = Button(text="Query", command=self.queryNetwork)
        self.btn_save.pack()
        self.btn_clear.pack()
        self.btn_query.pack()
        self.label_query_answer.pack()
        "Start the Loop"
        self.text_box.pack()
        self.root.mainloop()

    def save(self, path = "", saveWithAnswer = True):
        # 1.0 = einlesen des inputs von zeile 1 character 0, end-1c = lies bis zum ende und lösche den letzten character,
        # END fügt dem input string ein newline an das wir wieder löschen müssen
        correct_answer = self.text_box.get("1.0", "end-1c")
        if len(correct_answer) > 1:
            raise Exception("zu viele Zeichen, bitte nur Zahlen von 1-9")
        elif (not self.isnumber(correct_answer)) and saveWithAnswer:
            raise Exception("Bitte Zahl eingeben")
        if not path:
            path = self.savepath
        filename = path + correct_answer + self.current_save_number + ".png"

        imageResized = self.image1.resize(self.size, Image.ANTIALIAS)
        imageResized.save(filename)
        self.update_save_number()

    def clear(self):
        self.cv.delete("all")
        self.image1 = PIL.Image.new('L', (200, 200), "white")
        self.draw = ImageDraw.Draw(self.image1)
        self.text_box.delete("1.0", END)

    def paint(self, event):
        x1, y1 = (event.x), (event.y)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.cv.create_oval((x1, y1, x2, y2), fill='black', width=10)
        #  --- PIL
        self.draw.line((x1, y1, x2, y2), fill='black', width=10)

    def queryNetwork(self):
        path = "C:/temp/"
        self.save(path, saveWithAnswer=False)
        wandler = pngWandler(path)
        picture = wandler.openPictures()#TODO path definieren bei dem der Wandler die Bilder öffnen soll am besten mit setPath in der Wandler klasse
        answer = self.network.query(picture[1])
        formatted_answer = Helper.getIndexOfMaxValue(answer)
        self.label_query_answer.config(text=str(formatted_answer))
        print(formatted_answer)
        if path == "C:/":
            raise Exception("DONT DELETE ALL FOLDERS IN C")

        Helper.deleteFilesInFolder(path)


    @staticmethod
    def isnumber(some_string):
        try:
            int(some_string)
            return True
        except ValueError:
            return False

    def update_save_number(self):
        """Updated die Save nummer und schreibt sie direkt ins Sicherungsfile hinein"""
        helper = int(self.current_save_number)
        helper += 1
        "nummer wieder in String wandeln und abspeichern"
        self.current_save_number = str(helper)
        file = open(self.savepath + "currentImgCount.txt", "w+")
        file.write(self.current_save_number)
        file.close()
