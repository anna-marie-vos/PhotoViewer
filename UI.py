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
        self.counter = 0
        self.imageList=['item','item2','item3']
        # self.timeit = False
        # self.interval = 5000

        self.nextBtn = Button(self.window, text='back', width=6, command=lambda: self.goToPreviousImage("back"))
        self.nextBtn.pack(side=LEFT)

        self.getFolderBtn = Button(self.window, text = "Select a Folder", width = 12, command=self.getFolder)
        self.getFolderBtn.pack()

        # self.thirtySecTimer = Button(self.window, text='30 seconds', width=10, command=lambda: self.setCountdown(2))
        # self.thirtySecTimer.pack(side=BOTTOM)


        self.nextBtn = Button(self.window, text='next', width=6, command=lambda: self.goToNextImage("next"))
        self.nextBtn.pack(side=RIGHT)


    def getFolder(self):
        filename = filedialog.askdirectory()
        self.folderPath.set(filename)
        self.imageList = os.listdir(str(self.folderPath.get()))
        self.openImage()

    def openImage(self):
        self.img = self.imageList[self.counter]
        if self.img.lower().endswith(('.png', '.jpg', '.jpeg')):
            self.imagePath = (self.folderPath.get()+'/'+str(self.img))
            load = Image.open(self.imagePath)
            resized = load.resize((500,500),Image.ANTIALIAS)
            render = ImageTk.PhotoImage(resized)
            self.img = Label(self.window, width=500, height=500,image=render)
            self.img.image = render
            self.img.pack(side=BOTTOM)
        else:
            if self.buttonPress == "back":
                self.goToPreviousImage("back")
            else:
                self.goToNextImage("next")

    def goToNextImage (self, btnPress):
        self.buttonPress = "next"

        if not isinstance(self.img, str):
            self.img.destroy()

        if self.counter < len(self.imageList)-1:
            self.counter += 1
            self.openImage()

        elif self.counter == len(self.imageList)-1:
            self.counter = len(self.imageList)-1
            self.openImage()

    def goToPreviousImage (self, btnPress):
        self.buttonPress = btnPress
        if not isinstance(self.img, str):
            self.img.destroy()

        if self.counter > 0:
            self.counter -= 1
            self.openImage()

        elif self.counter == 0:
            self.counter = 0
            self.openImage()

    # def timeLoop(self):
    #     if self.timeit:
    #         self.window.after(self.interval, self.timeLoop)
    #
    # def getInterval(self):
    #     if self.timeInput.get() =="":
    #         self.interval = 5000
    #     else :
    #         self.interval = self.timeInput.get()*1000




root = Tk()
app = UI(root)
root.mainloop()
