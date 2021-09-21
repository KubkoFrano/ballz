import tkinter
import random

#private
state = 1
root = tkinter.Tk()
setCanvas = tkinter.Canvas(width=350, height=240)
workingCanvas = tkinter.Canvas()
hasCanvas = 0
xSet = 80
xEn = 160

#arrays


#create string variables
tHeight = tkinter.StringVar()
tWidth = tkinter.StringVar()
tBackSize = tkinter.StringVar()
tFrontSize = tkinter.StringVar()
tTimes = tkinter.StringVar()
tBackColor = tkinter.StringVar()
tFrontColor = tkinter.StringVar()
tBackgroundColor = tkinter.StringVar()
tText = tkinter.StringVar()

#settable
cHeight = 480
cWidth = 720
bigFontSize = 25
smallFontSize = 20
times = 1000
backColor = "cyan"
frontColor = "magenta"
backgroundColor = "magenta"
txt = "balls"

def setting():
    #create texts
    setCanvas.pack()
    setCanvas.create_text(xSet, 20, text="Height:")
    setCanvas.create_text(xSet, 40, text="Width:")
    setCanvas.create_text(xSet, 60, text="Back font size:")
    setCanvas.create_text(xSet, 80, text="Front font size:")
    setCanvas.create_text(xSet, 100, text="Instance count:")
    setCanvas.create_text(xSet, 120, text="Back font color:")
    setCanvas.create_text(xSet, 140, text="Front font color:")
    setCanvas.create_text(xSet, 160, text="Background color:")
    setCanvas.create_text(xSet, 180, text="Text:")

    #create input fields
    eHeight = tkinter.Entry(root, textvariable = tHeight).place(x = xEn, y = 10)
    eWidth = tkinter.Entry(root, textvariable = tWidth).place(x = xEn, y = 30)
    eBackSize = tkinter.Entry(root, textvariable = tBackSize).place(x = xEn, y = 50)
    eFrontSize = tkinter.Entry(root, textvariable = tFrontSize).place(x = xEn, y = 70)
    eTimes = tkinter.Entry(root, textvariable = tTimes).place(x = xEn, y = 90)
    eBackColor = tkinter.Entry(root, textvariable = tBackColor).place(x = xEn, y = 110)
    eFrontColor = tkinter.Entry(root, textvariable = tFrontColor).place(x = xEn, y = 130)
    eBackgroundColor = tkinter.Entry(root, textvariable = tBackgroundColor).place(x = xEn, y = 150)
    eText = tkinter.Entry(root, textvariable = tText).place(x = xEn, y = 170)

    #set default values
    tHeight.set(cHeight)
    tWidth.set(cWidth)
    tBackSize.set(bigFontSize)
    tFrontSize.set(smallFontSize)
    tTimes.set(times)
    tBackColor.set(backColor)
    tFrontColor.set(frontColor)
    tBackgroundColor.set(backgroundColor)
    tText.set(txt)

    #create button
    btn = tkinter.Button(root, text="BALLZ", command=ex)
    btn.place(x=xEn + 97, y=200)

def ex():
    #get new values
    tempHeight = int(tHeight.get())
    tempWidth = int(tWidth.get())
    tempBackgroundColor = tBackgroundColor.get()
    tempTxt = tText.get()
    tempBackColor = tBackColor.get()
    tempFrontColor = tFrontColor.get()
    tempBackSize = int(tBackSize.get())
    tempFrontSize = int(tFrontSize.get())
    tempTimes = int(tTimes.get())

    top = tkinter.Toplevel(root)
    bigFont = ("Arial", tempBackSize, "bold")
    smallFont = ("Arial", tempFrontSize, "bold")
    workingCanvas = tkinter.Canvas(top, height=tempHeight, width=tempWidth, bg=tempBackgroundColor)
    workingCanvas.pack()
    i = 0

    while(i < tempTimes):
        rX = random.randint(0, tempWidth)
        rY = random.randint(0, tempHeight)
                    
        workingCanvas.create_text(rX, rY, text=tempTxt, font=bigFont, fill=tempBackColor)
        workingCanvas.create_text(rX, rY, text=tempTxt, font=smallFont, fill=tempFrontColor)
        i+=1

    top.mainloop()

#main
setting()
root.mainloop()

