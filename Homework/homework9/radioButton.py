import tkinter

window = tkinter.Tk()

selectedButtonText = "one"   
choiceVar = tkinter.IntVar()
choiceVar.set(1)

def radioButtonChosen():
    global selectedButtonText
    if choiceVar.get() == 1:
        selectedButtonText = "one"
    else:
        selectedButtonText = "two"
    label.configure(text= "radio button choice is: {}".format(selectedButtonText))

choice1 = tkinter.Radiobutton(window, text="one", variable=choiceVar, value=1,
                  command=radioButtonChosen)
choice1.pack()

choice2 = tkinter.Radiobutton(window, text="two", variable=choiceVar, value=2,
                  command=radioButtonChosen)
choice2.pack()

label = tkinter.Label(window, text = "radio button choice is: {}".format(selectedButtonText))
label.pack()

def startGUI():
    global selectedButton
    window.mainloop()
startGUI()