import numpy as np
import tkinter as tk
from tkinter import ttk
import os

class studyApp:
    def __init__(self, root):
        self.root = root
        root.title("Study App")
        root.geometry("1000x600")
        root.resizable(width = False, height = False)
        root.configure(bg = "#3b3b3b")
        self.createFrame(self.root)

        self.questions = []

    # Create initial menu frame
    def createFrame(self, root):
        self.appFrame = tk.Frame(root,
                                 background = "#3b3b3b")
        self.appFrame.pack()        

        # Creates the title
        titleLabel = tk.Label(self.appFrame, 
                            text = "Welcome to the study tool!",
                            font = "impact 70",
                            background = "white",
                            fg = "black").pack()
        
        # Horizontal line below the title
        #hr = tk.Canvas(self.appFrame, height=5, bg='white', bd=0, highlightthickness=0)
        #hr.pack(fill='x', pady=5)

        # Button brings users to study set
        studyButton = tk.Button(self.appFrame,
                            text = "Study a set",
                            font = "impact 40",
                            command = self.studyClicked,
                            width = "12",
                            height = "3",
                            bg = "grey",
                            fg = "black")
        
        # Button brings users to create set
        createButton = tk.Button(self.appFrame,
                            text = "Create a set",
                            font = "impact 40",
                            command = lambda: self.createClicked(True),
                            width = "12",
                            height = "3")
                            
        
        studyButton.pack(side = "left", pady = "5")
        createButton.pack(side = "right", pady = "5")

    def createClicked(self, cond):
        # cond is a boolean: if false, means user attempted to submit a blank name for study set

        # clear frame in prepration for new contents 
        self.clearFrame()
        if cond == False:
            correctLbl = tk.Label(self.appFrame,
                                  text = "SET MUST BE NAMED!",
                                  font = "impact 70",
                                  background = "white",
                                  fg = "red")
            correctLbl.grid(row = 3, column = 0)
        
        studyLbl = tk.Label(self.appFrame,
                            text = "Enter the name of the set",
                            font = "impact 70",
                            background = "white",
                            fg = "black")
        
        self.studyName = tk.Entry(self.appFrame,
                             bg = "white",
                             fg = "black")

        submitName = tk.Button(self.appFrame,
                               text = "Submit",
                               command = self.addStudyTitle)
        
        studyLbl.grid(row = 0, column= 0)
        self.studyName.grid(row = 1, column= 0)
        submitName.grid(row = 2, column = 0)

    def createStudyCreate(self):
        userLbl = tk.Label(self.appFrame,
                           text = self.questions[0],
                           font = "impact 70",
                           background = "white",
                           fg = "black")
        
        userQuestion = tk.Label(self.appFrame,
                                text = "Question:",
                                font = "impact 30",
                                background = "white",
                                fg = "black")
        
        questionEntry = tk.Entry(self.appFrame,
                                 bg = "white",
                                 fg = "black")
        

        userLbl.grid(row = 0, column = 1)
        userQuestion.grid(row = 1, column = 0)
        questionEntry.grid(row = 1, column = 2)


    def addStudyTitle(self):
        # gets contents from the study set name entry box
        if self.studyName.get().strip() == "":
            self.createClicked(cond = False)
        else:
            self.questions.append(self.studyName.get())
            self.clearFrame()
            self.createStudyCreate()


    def studyClicked(self):
        # clear frame in prepration for new contents 
        self.clearFrame()

    # Empties frame to display new contents
    def clearFrame(self):
        for widget in self.appFrame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    window = tk.Tk()
    studyApp(window)
    window.mainloop()



