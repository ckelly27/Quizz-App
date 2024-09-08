import numpy as np
import tkinter as tk
import os


class studyApp:
    def __init__(self, root):
        self.root = root
        root.title("Study App")
        root.geometry("1000x600")
        root.resizable(width = False, height = False)
        appFrame = tk.Frame(root,
                            bg = '#ADD8E6')
        appFrame.pack()

        studyButton = tk.Button(root,
                            text = "Study a set",
                            bg = '#ADD8E6',
                            command = self.studyClicked(appFrame),
                            width = "60",
                            height = "10",
                            activebackground = "blue",
                            activeforeground = "blue")
                            
        
        studyButton.pack(side = "top")
<<<<<<< HEAD

    # button action
=======
    # button action hello
>>>>>>> 6f41daa84e1e403ed6356a8c146eea72798ad542
    def studyClicked(self, frame):
        pass


if __name__ == "__main__":
    window = tk.Tk()
    studyApp(window)
    window.mainloop()



