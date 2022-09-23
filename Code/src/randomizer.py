import random
from time import sleep
from tkinter import *
from tkinter import ttk


class RandomizeGUI():
    """
    RandomizeGUI initializes a Graphical User Interface (GUI) in which a
    User can let the Program select a random Element of a List of Choices.
    """

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
        """
        setRootConfigurations sets the initial values for the root Frame of the GUI
        including the initial position of the Frame.
        """
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
        """
        randomize Selects a Random element of the list of choices.

        Returns:
            str: The choice
        """
        return random.choice(self.choices)


    def updateRandomizer(self):
        """
        updateRandomizer Calls the randomize function of this class and updates
        the Label of the GUI with the returned choice.
        """
        randomChoice = self.randomize()
        self.displayChoiceLabel.config(text=randomChoice)
        self.displayChoiceLabel.update()
        
        
    def multiRandomize(self):
        """
        multiRandomize Calls the updateRandomizer function of this class multiple
        times in a progressing time period.
        """
        self.randomizeButton["state"] = "disabled"
        waitTime = 0.01
        
        while waitTime < 0.3:
            self.updateRandomizer()
            sleep(waitTime)
            waitTime = waitTime * 1.15
                
        self.randomizeButton["state"] = "active"        
        
        
    def start(self):
        """
        start Starts the mainloop of the Frame
        """
        self.root.mainloop()
        

randomizeGUI = RandomizeGUI()
randomizeGUI.start()

