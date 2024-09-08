import numpy as np
import tkinter as tk
import os


class studyApp:
    def __init__(self, root):
        self.root = root
        root.title("Study App")
        root.geometry("1000x600")
        root.resizable(width = False, height = False)
        self.createFrame(self.root)

    def createFrame(self, root):
        self.appFrame = tk.Frame(root)
        self.appFrame.pack()        

        titleLabel = tk.Label(self.appFrame, 
                            text = "Welcome to the study tool!",
                            font = "impact 70",).pack()
        
        hr = tk.Canvas(self.appFrame, height=5, bg='white', bd=0, highlightthickness=0)
        hr.pack(fill='x', pady=5)

        studyButton = tk.Button(self.appFrame,
                            text = "Study a set",
                            font = "impact 40",
                            command = self.studyClicked,
                            width = "12",
                            height = "3")
        
        createButton = tk.Button(self.appFrame,
                            text = "Create a set",
                            font = "impact 40",
                            command = self.studyClicked,
                            width = "12",
                            height = "3")
                            
        
        studyButton.pack(side = "top", pady = "5")
        createButton.pack(side = "top", pady = "5")

    def studyClicked(self):
        self.clearFrame()

    def createClicked(self):
        self.clearFrame()

    def clearFrame(self):
        for widget in self.appFrame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    window = tk.Tk()
    studyApp(window)
    window.mainloop()



