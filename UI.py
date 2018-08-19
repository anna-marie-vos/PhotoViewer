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
        self.timeit = False
        self.interval = 500


        self.getFolderBtn = Button(self.window, text = "Select a Folder", width = 12, command=self.getFolder)
        self.getFolderBtn.grid(row=1, column=3)

        self.backBtn = Button(self.window, text='back', width=6, command=lambda: self.goToPreviousImage("back"))
        self.backBtn.grid(row=2, column=1)

        self.nextBtn = Button(self.window, text='next', width=6, command=lambda: self.goToNextImage("next"))
        self.nextBtn.grid(row=2, column=5)

        self.displayCountdown = Label(self.window, text='', width =12)
        self.displayCountdown.grid(row=3,column=1)

        self.thirtySecTimer = Button(self.window, text='30 seconds', width=12, command=lambda: self.start(30000))
        self.thirtySecTimer.grid(row=3,column=2)

        self.sixtySecTimer = Button(self.window, text='60 seconds', width=12, command=lambda: self.start(60000))
        self.sixtySecTimer.grid(row=3,column=3)

        self.pause = Button(self.window, text='Stop', width=12, command=self.pause)
        self.pause.grid(row=3,column=4)



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
            self.resizeImg(load.size[0],load.size[1])
            resized = load.resize((self.newWidth, self.newHeight),Image.ANTIALIAS)
            render = ImageTk.PhotoImage(resized)
            self.img = Label(self.window, width=800, height=600,image=render)
            self.img.image = render
            self.img.grid(row=2,column=2, columnspan=3)

        else:
            if self.buttonPress == "back":
                self.goToPreviousImage("back")
            else:
                self.goToNextImage("next")

    def resizeImg(self,width,height):
        dividedByWidth = 800/width
        dividedByHeight = 600/height

        if dividedByWidth <= dividedByHeight:
            dividedBy = dividedByWidth
        else:
            dividedBy = dividedByHeight

        self.newWidth = int(width * dividedBy)
        self.newHeight = int(height * dividedBy)

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

    def start(self, setTime):
        self.interval = setTime
        self.timeit = True
        self.setCountdown()

    def pause(self):
        self.interval = 0
        self.timeit = False
        self.setCountdown()

    def setCountdown(self):
        if self.counter == len(self.imageList)-1:
            self.counter = -1

        if self.timeit:
            self.goToNextImage('next')
            self.displayTime(self.interval)
            root.after(self.interval, self.setCountdown)

    def displayTime(self, time):
        if time >0:
            if self.timeit:
                currentTime = time
                self.displayCountdown["text"]=('Timer: '+str(currentTime/1000))
                root.after(1000, self.displayTime, currentTime-1000)
            elif self.timeit:
                currentTime = self.interval
                self.displayCountdown["text"]=('Timer: '+str(currentTime/1000))
                root.after(1000, self.displayTime, currentTime-1000)
            else:
                self.displayCountdown["text"]='stopped'
        else:
            self.displayCountdown["text"]=('Timer: '+str(self.interval/1000))

root = Tk()
app = UI(root)
root.mainloop()
