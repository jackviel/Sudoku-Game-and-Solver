from tkinter import *
from tkinter import messagebox

# used by checkIfBoardIsCorrect, checks if a list has consecutive numbers
def checkIfListIsCorrect(list):
    tempList = list.copy()
    tempList.sort()
    for j in range(8):
        if (tempList[j] + 1 != tempList[j + 1]) or (tempList[j] < 1 or tempList[j] > 9):
            return False
        else:
            return True
# checks if the solution given is correct
def checkIfBoardIsCorrect():
    tempList = []

    for i in range(9):
        if checkIfListIsCorrect(sudokuBoard[i]) == False:
            messagebox.showinfo(title=None, message="Incorrect :'(")
            return

    for i in range(9):
        for j in range(9):
            tempList[j] = sudokuBoard[j][i]
        if checkIfListIsCorrect(sudokuBoard[i]) == False: 
            messagebox.showinfo(title=None, message="Incorrect :'(")
            return

    row = 0
    col = 0
    numCount = 0

    for i in range(9):
        for j in range(9):
            tempList[numCount] = sudokuBoard[row][col]
            numCount += 1
            col += 1
            if numCount == 9:
                if row == 8 and col % 3 == 0:
                    row = 0
                    numCount = 0
                    continue
            if col % 3 == 0:
                col -= 3
                row += 1
            if numCount == 9:
                if checkIfListIsCorrect(tempList[i]) == False:
                    messagebox.showinfo(title=None, message="Incorrect :'(")
                    return
                numCount = 0
    messagebox.showinfo(title=None, message="Correct! :)")
# used by solveSudoku, checks if the number given is possible, checks
# if n is in either the row or column, then checks each 3x3 square.
def checkIfNumIsPossible(x,y,n):
    for i in range(9):
        if sudokuBoard[x][i] == n:
            return False
    for i in range(9):
        if sudokuBoard[i][y] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if sudokuBoard[x0+1][y0+j] == n:
                return False
    return True
# solves the sudoku using recursion and backtracking, then changes the gui
def solveSudoku():
    for i in range(9):
        for j in range(9):
            if sudokuBoard[i][j] == 0:
                for n in range(1,10):
                    if checkIfNumIsPossible(i,j,n):
                        sudokuBoard[i][j] = n
                        solveSudoku()
                        sudokuBoard[i][j] = 0
                return
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, END)
            entries[i][j].insert(0, sudokuBoard[i][j])
            entries[i][j].config(state="disabled")
    return
# checks the numbers inputted and changes the sudoku board
def changeCell():
    for i in range(9):
        for j in range(9):
            if (entries[i][j].get() != ""):
                sudokuBoard[i][j] = int(entries[i][j].get())
                entries[i][j].config(state="disabled")

# initialize sudoku board
sudokuBoard = [[0 for i in range(9)] for j in range(9)]
# create gui window
root = Tk()
root.title("Sudoku Game & Solver")
# create main frame
frame = LabelFrame(root)
frame.grid(padx=2, pady=2,row=0, column=0)
# list with all of the entries
entries = []
# create all sudoku entries and add them to the list
for i in range(9):
    entryRow = []
    for j in range(9):
        curEntry = Entry(frame, width=2)
        curEntry.grid(row=i, column=j, padx = 5, pady = 5)
        entryRow.append(curEntry)
    entries.append(entryRow)
# create set entries button
setButton = Button(root, text="Set Puzzle", command=changeCell)
setButton.grid(row=9,column=0)
# create check if entries are correct button
checkButton = Button(root, text="Check if correct", command=checkIfBoardIsCorrect)
checkButton.grid(row=10, column=0)
# create the solver button
solveButton = Button(root, text="Solve Sudoku", command=solveSudoku)
solveButton.grid(row=11, column=0)
# gui mainloop
root.mainloop()