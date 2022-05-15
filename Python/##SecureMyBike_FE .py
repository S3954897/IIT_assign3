#IIT Assignment3 SecureMyBike_FE.py v1.08may22 author:grantn

import SecureMyBike_BE as bE
import tkinter as tk
from tkinter import Tk, messagebox
backend = bE.UserManager()
app = Tk()



class DefaultFrame:
    def __init__(self, myTitle) -> None:
        LARGE_FONT = ("Arial", 20,"bold")
        MED_FONT = ("Arial", 16)
        self.myFrame = Frame()
        self.myFrame.title(myTitle)
        self.myFrame.pack()
        
class AppUI:
    def __init__(self):
        #window1 = DefaultFrame("Test")

        pass
        

       



app.mainloop()

        
