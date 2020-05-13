import tkinter, random
class Global:
	problemAns,problemtxt,gameWindow,button,guess = None,None,None,None,None
	attemptsLabel,solvedLabel,averageLabel,statusLabel = None,None,None,None
	guessNumber = 0
	incorrect = 0
	incorrectTotal = 0
	attempts = 1
	solved = 0
	attemptsLabel = None
	solvedLabel = None
	averageLabel = None
	listOfUsed = []

def av():
	guessNumber, attempts = Global.guessNumber, Global.attempts
	return guessNumber / attempts

def initializeGameWindo():
	Global.gameWindow = tkinter.Tk()
	window = Global.gameWindow
	window.title("Cool Math Game")

	topFrame = tkinter.Frame(window)
	topFrame.pack()
	bottomFrame = tkinter.Frame(window)
	bottomFrame.pack()
	leftBottom = tkinter.Frame(bottomFrame)
	leftBottom.pack(side=tkinter.LEFT)
	rightBottom = tkinter.Frame(bottomFrame)
	rightBottom.pack()

	Global.problemtxt = tkinter.Label(topFrame)
	problemtxt = Global.problemtxt
	problemtxt.pack(side=tkinter.LEFT)
	Global.guess = tkinter.Entry(topFrame)
	guess = Global.guess
	guess.pack(side=tkinter.LEFT)
	button = Global.button
	button = tkinter.Button(topFrame, text='Check', command=checkGuess)
	button.pack()

	attemptsLabel, incorrect, solvedLabel = Global.attemptsLabel , Global.incorrect, Global.solvedLabel
	attemptsLabel = tkinter.Label(leftBottom, text=f'Attempts this problem: {incorrect}')
	attemptsLabel.pack()
	solvedLabel = tkinter.Label(leftBottom, text=f'Solved: {solved}')
	solvedLabel.pack()
	averageLabel = tkinter.Label(leftBottom, text=f'Average: {av()}')
	averageLabel.pack()