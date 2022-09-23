from mimetypes import init
import random
from time import sleep
from tkinter import *
from tkinter import ttk
from turtle import title, width, window_height, window_width


class RandomizeGUI():

    def __init__(self):
        # Set some Variables
        self.choices = ["TOP", "JNG", "MID", "ADC", "SUP"]
        
        
        self.root = Tk()
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.grid()

        self.displayChoiceLabel = ttk.Label(self.frame, text="", padding=10)
        self.randomizeButton = ttk.Button(self.frame, text="Spin", command=self.multiRandomize, width=20)

        self.setRootConfigurations()
        
        self.displayChoiceLabel.grid(column=0, row=0)
        self.randomizeButton.grid(column=0, row=1)
        
        # Center all Components
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        
    def setRootConfigurations(self):
        root = self.root
        root.title("Randomizer")   # Set Title
        root.resizable(False, False)   # Set Non-Resizeable
        
        # Center Window in Screen
        self.window_height = 175
        self.window_width = 350
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        
        x_cordinate = int((self.screen_width/2) - (self.window_width/2))
        y_cordinate = int((self.screen_height/2) - (self.window_height/2))
        root.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, x_cordinate, y_cordinate))
        
        
    def randomize(self):
        return random.choice(self.choices)


    def updateRandomizer(self):
        randomChoice = self.randomize()
        self.displayChoiceLabel.config(text=randomChoice)
        self.displayChoiceLabel.update()
        
        
    def multiRandomize(self):
        self.randomizeButton["state"] = "disabled"
        waitTime = 0.01
        
        while waitTime < 0.3:
            self.updateRandomizer()
            sleep(waitTime)
            waitTime = waitTime * 1.15
                
        self.randomizeButton["state"] = "active"        
        
        
    def start(self):
        self.root.mainloop()
        

randomizeGUI = RandomizeGUI()
randomizeGUI.start()

