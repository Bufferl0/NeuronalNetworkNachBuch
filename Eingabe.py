from tkinter import *
# by Canvas I can't save image, so i use PIL
import PIL
from PIL import Image, ImageDraw

# --Created by Janek Zitzmann, 18.09.2019
class Eingabe:
    def __init__(self,savepath):
        self.size = (28,28)
        self.savepath = savepath
        file = open("C:/pythonImg/currentImgCount.txt", "w+")
        self.current_save_number = file.read()
        "falls das file leer ist wird 0 als filename angesetzt und in das file geschrieben"
        if not self.current_save_number: # empty strings are considered false in boolean
            self.current_save_number = "0"
            file.write(str(self.current_save_number))

        file.close()
        self.root = Tk()
        self.cv = Canvas(self.root, width=200, height=200, bg='white')
        # --- PIL
        self.image1 = PIL.Image.new('RGB', (200, 200), 'white')
        self.draw = ImageDraw.Draw(self.image1)
        # ----
        self.cv.bind('<B1-Motion>', self.paint)
        self.cv.pack(expand=YES, fill=BOTH)
        "Button_init"
        self.btn_save = Button(text="save", command=self.save)
        self.btn_clear = Button(text="Clear", command=self.clear)
        self.text_box = Text(self.root, height=2, width=4)
        self.text_box.pack()
        self.btn_save.pack()
        self.btn_clear.pack()
        "Start the Loop"
        self.root.mainloop()

    def save(self):
        # 1.0 = einlesen des inputs von zeile 1 character 0, end-1c = lies bis zum ende und lösche den letzten character, END fügt dem input string ein newline an das wir wieder löschen müssen
        correct_answer= self.text_box.get("1.0", "end-1c")
        if len(correct_answer) > 1:
            raise Exception("zu viele Zeichen, bitte nur Zahlen von 1-9")
        elif not self.isnumber(correct_answer):
            raise Exception("Bitte Zahl eingeben")

        filename = self.savepath + correct_answer + self.current_save_number + ".png"
        self.update_save_number()
        imageResized = self.image1.resize(self.size, Image.ANTIALIAS)
        imageResized.save(filename)

    def clear(self):
        self.cv.delete("all")
        self.image1 = PIL.Image.new('RGB', (200, 200), 'white')
        self.draw = ImageDraw.Draw(self.image1)
        self.text_box.delete("1.0", END)

    def paint(self, event):
        x1, y1 = (event.x), (event.y)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.cv.create_oval((x1, y1, x2, y2), fill='black', width=10)
        #  --- PIL
        self.draw.line((x1, y1, x2, y2), fill='black', width=10)

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
        file = open(self.savepath + "currentImgCount.txt", "w")
        file.write(self.current_save_number)
        file.close()
