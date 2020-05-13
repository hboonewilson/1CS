import tkinter
import random

problemAns = None
problemtxt = None
gameWindow = None
button = None
statusLabel = None
guess = None
guessNumber = 0
incorrect = 0
incorrectTotal = 0
attempts = 1
solved = 0
attemptsLabel = None
solvedLabel = None
averageLabel = None
listOfUsed = []


def findNewProb(): 
	global attempts,incorrect
	incorrect = 0
	attempts += 1
	createRandProblem()

def quitGame():
	global gameWindow
	gameWindow.destroy()

def createRandProblem():
	global problemAns,problemtxt,attempts,attemptsLabel,averageLabel,listOfUsed
	problemString = None
	while problemString == None or problemString in listOfUsed:
		operators = ['+','-','/','*']
		operatorD = {'+': add, '-': sub, '/': div, '*': mult}
		op = operators[random.randint(0,3)]
		problemAns, problemString = operatorD[op]()
	toRound = av()
	rounded = round(toRound, 2)
	averageLabel.configure(text=f'AnsAttempts/Problem: {rounded}')
	listOfUsed.append(problemString)
	button.configure(command=checkGuess)
	statusLabel.configure(text='Not attempted')
	attemptsLabel.configure(text=f'Attempts Current Problem:  {incorrect}')
	problemtxt.configure(text=f"{problemString}")
	button.configure(state=tkinter.NORMAL)

def av():
	global guessNumber, attempts
	return guessNumber / attempts
	

def checkGuess():
	global problemAns,averageLabel,button,solvedLabel,solved,guess
	global attemptsLabel,incorrect, incorrectTotal,guessNumber
	guessNumber += 1
	guessAsString = guess.get()
	guessInt = int(guessAsString)
	if guessInt == problemAns:
		button.configure(state=tkinter.DISABLED)
		statusLabel.configure(text= f"{guessInt} is correct!")
		solved += 1
		solvedLabel.configure(text=f'Solved: {solved}')
	else:
		incorrect += 1
		incorrectTotal += 1
		attemptsLabel.configure(text=f"Attempts Current Problem: {incorrect}")
		statusLabel.configure(text= f"{guessInt} is incorrect.")
	toRound = av()
	rounded = round(toRound, 2)
	averageLabel.configure(text=f'AnsAttempts/Problem: {rounded}')
	guess.delete(0, tkinter.END)

def add():
		n1 = random.randint(0, 1000)
		n2 = random.randint(0, 1000)
		return (n1 + n2), f'{n1} + {n2}'
def sub():
	n1 = None
	n2 = None
	while n1 == None or n1 < n2:
		n1 = random.randint(0, 1000)
		n2 = random.randint(0, 1000)
	return (n1 - n2), f'{n1} - {n2}'
def div():
	n1 = None
	n2 = None
	divisibleBy = False
	while n1 == None or divisibleBy == False:
		n1 = random.randint(0, 1000)
		n2 = random.randint(1, 1000)
		if n1 >= n2:
			if n1 == 0:
				divisibleBy = True
				
			if (n1 % n2) == 0:
				divisibleBy = True
	return int(n1 / n2), f'{n1} / {n2}'
def mult():
	n1 = random.randint(0, 100)
	n2 = random.randint(0, 100)
	return (n1 * n2), f'{n1} x {n2}'


def window():
	global gameWindow, problemString,button,statusLabel
	global solvedLabel,attemptsLabel,guess,averageLabel,problemtxt,incorrect

	gameWindow = tkinter.Tk()
	gameWindow.title('Math Game')


	topFrame = tkinter.Frame(gameWindow)
	topFrame.pack()

	problemtxt = tkinter.Label(topFrame)
	problemtxt.pack(side=tkinter.LEFT)
	guess = tkinter.Entry(topFrame)
	guess.pack(side=tkinter.LEFT)
	button = tkinter.Button(topFrame, text='Check', command=checkGuess)
	button.pack()


	bottomFrame = tkinter.Frame(gameWindow)
	bottomFrame.pack()

	leftSide = tkinter.Frame(bottomFrame)
	leftSide.pack(side=tkinter.LEFT)
	attemptsLabel = tkinter.Label(leftSide, text=f'Attempts this problem: {incorrect}')
	attemptsLabel.pack()
	solvedLabel = tkinter.Label(leftSide, text=f'Solved: {solved}')
	solvedLabel.pack()
	ave = av()
	averageLabel = tkinter.Label(leftSide, text=f'Average: {ave}')
	averageLabel.pack()

	rightSide = tkinter.Frame(bottomFrame)
	rightSide.pack()
	statusLabel = tkinter.Label(rightSide, text="Not attemted.")
	statusLabel.pack()
	newProbButton = tkinter.Button(rightSide,text='New Problem', command=findNewProb)
	newProbButton.pack()
	quitGameButton = tkinter.Button(rightSide, text='Quit Game', command=quitGame)
	quitGameButton.pack()

def startGameGUI():
	global attempts, solved, incorrectTotal
	window()
	createRandProblem()
	gameWindow.mainloop()
	print('Problems Attempted: ', attempts)
	print('Problems Solved: ', solved)
	rounded = round(incorrectTotal/attempts)
	print('Average (Incorrect attempts)/problem)): ', rounded)

