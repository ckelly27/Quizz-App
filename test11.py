import numpy as np
import tkinter as tk
from tkinter import ttk
import csv
import os

class studyApp:
    def __init__(self, root):
        self.root = root
        root.title("Study App")
        root.geometry("1000x600")
        root.resizable(width = False, height = False)
        root.configure(bg = "#3b3b3b")
        self.setName = ""
        self.questions = []
        self.qCount = 1
        self.createFrame()

    # Create initial menu frame
    def createFrame(self):
        self.appFrame = tk.Frame(self.root,
                                 background = "#3b3b3b")
        self.appFrame.pack()        

        # Creates the title
        titleLabel = tk.Label(self.appFrame, 
                            text = "Welcome to the study tool!",
                            font = "impact 70",
                            background = "white",
                            fg = "black")
        
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
                            
        titleLabel.grid(row = 0, column = 0)
        studyButton.grid(row = 1, column = 0)
        createButton.grid(row = 2, column = 0)

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

    def createStudyCreate(self, cond):
        userLbl = tk.Label(self.appFrame,
                           text = self.setName + " Study Set",
                           font = "impact 70",
                           background = "white",
                           fg = "black")
        
        self.questionEntry = tk.Entry(self.appFrame,
                                 bg = "white",
                                 fg = "black")
        qNumStr = "Question " + str(self.qCount)
        self.questionEntry.insert(0, qNumStr)

        self.a1 = tk.Entry(self.appFrame,
                      bg = "white",
                      fg = "black")
        self.a1.insert(0, "answer 1")

        self.a2 = tk.Entry(self.appFrame,
                      bg = "white",
                      fg = "black")
        self.a2.insert(0, "answer 2")

        self.a3 = tk.Entry(self.appFrame,
                      bg = "white",
                      fg = "black")
        self.a3.insert(0, "answer 3")

        self.a4 = tk.Entry(self.appFrame,
                      bg = "white",
                      fg = "black")
        self.a4.insert(0, "answer 4")

        self.answer = tk.Entry(self.appFrame,
                      bg = "white",
                      fg = "black")
        self.answer.insert(0, "Which is the correct answer? 1, 2, 3, 4?")

        submit = tk.Button(self.appFrame,
                          text = "submit",
                          background = "white",
                          fg = "black",
                          command = self.submitQuestion)


        validAnswer = tk.Label(self.appFrame,
                                   text = "Enter 1, 2, 3, or 4 for the correct answer!",
                                   font = "impact 40",
                                   background = "white",
                                   fg = "red")
        
        finishBtn = tk.Button(self.appFrame,
                              text = "Finish",
                              background = "white",
                              fg = "black",
                              command = self.finishSet)

        userLbl.grid(row = 0, column = 0)
        self.questionEntry.grid(row = 1, column = 0)
        self.a1.grid(row = 2, column = 0)
        self.a2.grid(row = 3, column = 0)
        self.a3.grid(row = 4, column = 0)
        self.a4.grid(row = 5, column = 0)
        self.answer.grid(row = 6, column = 0)
        submit.grid(row = 7, column = 0)
        if self.qCount != 1:
            finishBtn.grid(row = 8, column = 0)

        if cond == False:
            validAnswer.grid(row = 9, column = 0)

    def finishSet(self):
        headers = ["Question", "Answer 1", "Answer 2", "Answer 3", "Answer 4", "Correct Answer"]
        with open(self.csv_file, mode = "w", newline = "", encoding = "utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(headers)

            for i in range(0, len(self.questions), 6):
                row = self.questions[i:i+6]
                writer.writerow(row)
        
        self.clearFrame()

        confirmationLbl = tk.Label(self.appFrame,
                                   text = "The file has been saved!",
                                   font = "impact 70",
                                   background = "white",
                                   fg = "black")
        
        homeBtn = tk.Button(self.appFrame,
                            text = "Return Home",
                            background = "white",
                            fg = "black",
                            command = self.createFrame)
        

        confirmationLbl.grid(row = 0, column = 0)
        homeBtn.grid(row = 1, column = 0)


    def submitQuestion(self):
        if self.answer.get().strip() not in ['1', '2', '3', '4']:
            self.createStudyCreate(False)
        else:
            self.questions.append(self.questionEntry.get())
            self.questions.append(self.a1.get())
            self.questions.append(self.a2.get())
            self.questions.append(self.a3.get())
            self.questions.append(self.a4.get())
            self.questions.append(self.answer.get())
            self.qCount += 1
            self.clearFrame()
            self.createStudyCreate(True)

    def addStudyTitle(self):
        # gets contents from the study set name entry box
        if self.studyName.get().strip() == "":
            self.createClicked(cond = False)
        else:
            self.setName = self.studyName.get()
            self.csv_file = self.setName + ".csv"
            self.clearFrame()
            self.createStudyCreate(True)


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



