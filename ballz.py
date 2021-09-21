import tkinter
import random

root = tkinter.Tk()
state = 1

cHeight = 480
cWidth = 720
bigFontSize = 25
smallFontSize = 20
times = 1000

backColor = "cyan"
frontColor = "magenta"
backgroundColor = "magenta"
txt = "balls"

print("Welcome to background maker ...")
print("Properties: height, width, backSize, frontSize, times, backColor, frontColor, backgroundColor, text, quit")
print("   height =>", cHeight)
print("   width =>", cWidth)
print("   backSize =>", bigFontSize)
print("   frontSize =>", smallFontSize)
print("   times =>", times)
print("   backColor =>", backColor)
print("   frontColor =>", frontColor)
print("   backgroundColor =>", backgroundColor)
print("   text =>", txt)
print("type ballz to initiate ...")

workingCanvas = tkinter.Canvas(height=cHeight, width=cWidth, bg=backgroundColor)

while (1):
    if (state == 0):
        root.destroy()
        break
    
    workingCanvas.destroy()
    bigFont = ("Arial", bigFontSize, "bold")
    smallFont = ("Arial", smallFontSize, "bold")
    workingCanvas = tkinter.Canvas(height=cHeight, width=cWidth, bg=backgroundColor)
    workingCanvas.pack()
    i = 0

    while(i < times):
        rX = random.randint(0, cWidth)
        rY = random.randint(0, cHeight)
                    
        workingCanvas.create_text(rX, rY, text=txt, font=bigFont, fill=backColor)
        workingCanvas.create_text(rX, rY, text=txt, font=smallFont, fill=frontColor)
        i+=1
    
    while(1):
        usrIn = input()

        if (usrIn == "ballz"):
            break
        elif (usrIn == "times"):
            times = int(input("number of text instances: "))
        elif (usrIn == "height"):
            cHeight = int(input("canvas height: "))
        elif (usrIn == "width"):
            cWidth = int(input("canvas width: "))
        elif (usrIn == "backSize"):
            bigFontSize = int(input("back font size: "))
        elif (usrIn == "frontSize"):
            smallFontSize = int(input("front font size: "))
        elif (usrIn == "backColor"):
            backColor = input("back font color: ")
        elif (usrIn == "frontColor"):
            frontColor = input("front font color: ")
        elif (usrIn == "backgroundColor"):
            backgroundColor = input("background color: ")
        elif (usrIn == "text"):
            txt = input("text: ")
        elif (usrIn == "quit"):
            state = 0
            break
                

root.mainloop()

