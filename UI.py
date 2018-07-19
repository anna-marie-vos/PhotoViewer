from tkinter import *
from tkinter import filedialog
# from tkCommonDialog import Dialog


class UI:
    def __init__(self,window):
        self.window = window
        self.window.minsize(width=600, height=500)
        self.window.wm_title("Photo Viewer")
        self.folderPath = StringVar()

        self.getFolderBtn = Button(self.window, text = "Select a Folder", width = 12, command=self.getFolder)
        self.getFolderBtn.pack()
        self.getFolderBtn.place(x = 420, y = 420)

    def getFolder(self):
        filename = filedialog.askdirectory()
        # self.folderPath.set(filename)
        # print(self.folderPath)

# Code to add widgets will go here...


root = Tk()
app = UI(root)
root.mainloop()
