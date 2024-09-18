import tkinter as tk
from tkinter import ttk
import csv
import os
from tkinter import filedialog

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

    # Creates screen where user enters name of study set
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

    # Creates screen where user enters the contents of the study set, question by question
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

        # Answer must be 1, 2, 3, or 4
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

        # Displays message that tells user answer must be 1, 2, 3, 4
        if cond == False:
            validAnswer.grid(row = 9, column = 0)

    # Saves the study set as a CSV for later use
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
                                   text = "The file has been saved as",
                                   font = "impact 70",
                                   background = "white",
                                   fg = "green")
        
        fileLbl = tk.Label(self.appFrame,
                                   text = self.csv_file,
                                   font = "impact 70",
                                   background = "white",
                                   fg = "green")
        
        homeBtn = tk.Button(self.appFrame,
                            text = "Return Home",
                            background = "white",
                            fg = "black",
                            command = lambda: [self.clearFrame(),
                                               self.appFrame.destroy(),
                                               self.createFrame()])
        

        confirmationLbl.grid(row = 0, column = 0)
        fileLbl.grid(row = 1, column = 0)
        homeBtn.grid(row = 2, column = 0)

    # Submits question with answers and appends to list of questions
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

    # Ensures title isnt blank and sets CSV file name
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
        self.questions = []

        # Clear frame in prepration for new contents 
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv")],
            title="Select a Study Set"
        )
        self.csv_file = file_path

        self.clearFrame()
        try:
            with open(self.csv_file, mode='r', newline='', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                headers = next(csv_reader) 
                for row in csv_reader:
                    if row:
                        self.questions.append(row)
                        
        # If some error occurs during file selection, goes to home screen                
        except:
            self.appFrame.destroy()
            self.createFrame()

        self.currQuestion = 0
        self.displayQuestions()
        
        # If user hits cancel during file selection
        if not file_path:
            self.appFrame.destroy()
            self.createFrame()
    
    # Displays questions and respective answers
    def displayQuestions(self):

        # If out of questions, tells user
        if self.currQuestion >= len(self.questions):
            self.clearFrame()
            doneLbl = tk.Label(self.appFrame,
                               text = "Out of Questions!",
                               font = "impact 70",
                               background = "white",
                               fg = "black")
            doneLbl.grid(row = 0, column = 0)
        else:    
            tempQ = self.questions[self.currQuestion][0]
            tempa1 = self.questions[self.currQuestion][1]
            tempa2 = self.questions[self.currQuestion][2]
            tempa3 = self.questions[self.currQuestion][3]
            tempa4 = self.questions[self.currQuestion][4]
            self.tempCorrect = self.questions[self.currQuestion][5]

            setName = os.path.basename(self.csv_file).replace(".csv", "")
            setLbl = tk.Label(self.appFrame,
                            text = setName + " set",
                            font = "impact 70",
                            background = "white",
                            fg = "black")
        
            qLbl = tk.Label(self.appFrame,
                            text = tempQ,
                            font = "impact 40",
                            background = "white",
                            fg = "black")
        
            self.a1Btn = tk.Button(self.appFrame,
                            text = tempa1,
                            background = "white",
                            fg = "black",
                            command = lambda: self.answerClicked(1))
            self.a2Btn = tk.Button(self.appFrame,
                            text = tempa2,
                            background = "white",
                            fg = "black",
                            command = lambda: self.answerClicked(2))
            self.a3Btn = tk.Button(self.appFrame,
                            text = tempa3,
                            background = "white",
                            fg = "black",
                            command = lambda: self.answerClicked(3))
            self.a4Btn = tk.Button(self.appFrame,
                            text = tempa4,
                            background = "white",
                            fg = "black",
                            command = lambda: self.answerClicked(4))
        
            self.nextQ = tk.Button(self.appFrame,
                                text = "Next question",
                                background = "white",
                                fg = "black",
                                command = self.nextQuestion)

            setLbl.grid(row = 0, column = 0)
            qLbl.grid(row = 1, column = 0)
            self.a1Btn.grid(row = 2, column = 0)
            self.a2Btn.grid(row = 3, column = 0)
            self.a3Btn.grid(row = 4, column = 0)
            self.a4Btn.grid(row = 5, column = 0)
            self.nextQ.grid(row = 7, column = 0)

    # Changes current question index and clears frame for next quesion and answers
    def nextQuestion(self):
        self.currQuestion += 1
        self.clearFrame()
        self.displayQuestions()
        
    def answerClicked(self, choice):
        # Button text becomes green if correct option is clicked
        if str(choice) == self.tempCorrect:
            if choice == 1:
                self.a1Btn.config(fg = "green")
            elif choice == 2:
                self.a2Btn.config(fg = "green")
            elif choice == 3:
                self.a3Btn.config(fg = "green")
            elif choice == 4:
                self.a4Btn.config(fg = "green")

        # Button text becomes red if incorrect option is clicked
        else:
            if choice == 1:
                self.a1Btn.config(fg = "red")
            elif choice == 2:
                self.a2Btn.config(fg = "red")
            elif choice == 3:
                self.a3Btn.config(fg = "red")
            elif choice == 4:
                self.a4Btn.config(fg = "red")


    # Empties frame to display new contents
    def clearFrame(self):
        for widget in self.appFrame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    window = tk.Tk()
    studyApp(window)
    window.mainloop()



