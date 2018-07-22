from tkinter import *
from tkinter import filedialog
import os
from PIL import ImageTk, Image
import time


class UI:
    def __init__(self,window):
        self.window = window
        self.window.minsize(width=600, height=500)
        self.window.wm_title("Photo Viewer")
        self.folderPath = StringVar()
        self.imagePath = ''

        self.getFolderBtn = Button(self.window, text = "Select a Folder", width = 12, command=self.getFolder)
        self.getFolderBtn.pack()

        self.folderLabel = Label(self.window,textvariable=self.folderPath)
        self.folderLabel.pack()

    def getFolder(self):
        filename = filedialog.askdirectory()
        self.folderPath.set(filename)
        self.imageList = os.listdir(str(self.folderPath.get()))
        self.openImage()

    def openImage(self):
        for img in self.imageList:
            if img.lower().endswith(('.png', '.jpg', '.jpeg')):
                self.imagePath = (self.folderPath.get()+'/'+str(img))
                print(self.imagePath)
                load = Image.open(self.imagePath)
                resized = load.resize((500,500),Image.ANTIALIAS)
                render = ImageTk.PhotoImage(resized)
                img = Label(self.window, width=500, height=500,image=render)
                img.image = render
                img.place(x=0, y=0)


root = Tk()
app = UI(root)
root.mainloop()
