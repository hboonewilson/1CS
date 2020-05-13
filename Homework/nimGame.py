from homework6 import NimGame as NG 
import tkinter

def getBoard():
	return nimGame.getName()

def pushButton():
	entry1 = int(entry1.get())
	entry2 = int(entry2.get())
	nimGame.remove(entry1, entry2)


mainwindow = tkinter.Tk()
nimGame = NG([1,3,5,7,9])


topFrame = tkinter.Frame(mainwindow)
topFrame.pack()

label1 = tkinter.Label(topFrame, text='Game Board:')
label1.pack(side=tkinter.LEFT)

currentState = getBoard()

label2 = tkinter.Label(topFrame, text=currentState)
label2.pack()
middleFrame=tkinter.Frame(mainwindow)
middleFrame.pack()
bottomFrame=tkinter.Frame(mainwindow)
bottomFrame.pack()

entry1 = tkinter.Entry(middleFrame)
entry1.pack(side=tkinter.LEFT)
entry2 = tkinter.Entry(bottomFrame)
entry2.pack(side=tkinter.LEFT)

button = tkinter.Button(middleFrame, text='Enter', command=pushButton)
button.pack()

mainwindow.mainloop()