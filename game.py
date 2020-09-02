import random as rand
#user is o
#ai is x
row1 = ["   ","   ","   "]
row2 = ["-----------"]
row3 = ["   ","   ","   "]
row4 = ["-----------"]
row5 = ["   ","   ","   "]
wholeBoard = [row1,row3,row5]
playerMove = 1
aIMove = 1
def playerTurn(wholeBoard):
    row = int(input("Enter a row going 1 to 3 downwards:")) - 1
    column = int(input("Enter a column going 1 to 3 rightwards:")) - 1
    wholeBoard[row][column] = " o "
    return wholeBoard
def aITurn(wholeBoard,aIMove):
    if (aIMove == 1):
        i = rand.randint(0, len(wholeBoard)-1)
        j = rand.randint(0, len(wholeBoard[i])-1)
        if wholeBoard[i][j] == "   ":
            wholeBoard[i][j] = " x "
        else:
            while (wholeBoard[i][j] != "   "):
                i = rand.randint(0, len(wholeBoard)-1)
                j = rand.randint(0, len(wholeBoard[i])-1)
    #vert and horiz with space in between
    elif (wholeBoard[0][0] == wholeBoard[0][2] and wholeBoard[0][0] == " x ") and wholeBoard[0][1] == "   ":
        wholeBoard[0][1] = " x "
    elif (wholeBoard[1][0] == wholeBoard[1][2] and wholeBoard[1][0] == " x ") and wholeBoard[1][1] == "   ":
        wholeBoard[1][1] = " x "
    elif (wholeBoard[2][0] == wholeBoard[2][2] and wholeBoard[2][0] == " x ") and wholeBoard[2][1] == "   ":
        wholeBoard[2][1] = " x "
    elif (wholeBoard[0][0] == wholeBoard[2][0] and wholeBoard[0][0] == " x ") and wholeBoard[1][0] == "   ":
        wholeBoard[1][0] = " x "
    elif (wholeBoard[0][1] == wholeBoard[2][1] and wholeBoard[0][1] == " x ") and wholeBoard[1][1] == "   ":
        wholeBoard[1][1] = " x "
    elif (wholeBoard[0][2] == wholeBoard[2][2] and wholeBoard[0][2] == " x ") and wholeBoard[1][2] == "   ":
        wholeBoard[1][2] = " x "
    elif (wholeBoard[0][0] == wholeBoard[2][2] and wholeBoard[0][0] == " x ") and wholeBoard[1][1] == "   ":
        wholeBoard[1][1] = " x "
    elif (wholeBoard[0][2] == wholeBoard[2][0] and wholeBoard[0][2] == " x ") and wholeBoard[1][1] == "   ":
        wholeBoard[1][1] = " x "
    #defensive blocking o with space in between
    elif (wholeBoard[0][0] == wholeBoard[0][2] and wholeBoard[0][0] == " o ") and wholeBoard[0][1] == "   ":
        wholeBoard[0][1] = " x "
    elif (wholeBoard[1][0] == wholeBoard[1][2] and wholeBoard[1][0] == " o ") and wholeBoard[1][1] == "   ":
        wholeBoard[1][1] = " x "
    elif (wholeBoard[2][0] == wholeBoard[2][2] and wholeBoard[2][0] == " o ") and wholeBoard[2][1] == "   ":
        wholeBoard[2][1] = " x "
    elif (wholeBoard[0][0] == wholeBoard[2][0] and wholeBoard[0][0] == " o ") and wholeBoard[1][0] == "   ":
        wholeBoard[1][0] = " x "
    elif (wholeBoard[0][1] == wholeBoard[2][1] and wholeBoard[0][1] == " o ") and wholeBoard[1][1] == "   ":
        wholeBoard[1][1] = " x "
    elif (wholeBoard[0][2] == wholeBoard[2][2] and wholeBoard[0][2] == " o ") and wholeBoard[1][2] == "   ":
        wholeBoard[1][2] = " x "
    elif (wholeBoard[0][0] == wholeBoard[2][2] and wholeBoard[0][0] == " o ") and wholeBoard[1][1] == "   ":
        wholeBoard[1][1] = " x "
    elif (wholeBoard[0][2] == wholeBoard[2][0] and wholeBoard[0][2] == " o ") and wholeBoard[1][1] == "   ":
        wholeBoard[1][1] = " x "
    #first 2 in row x
    elif (wholeBoard[0][0] == wholeBoard[0][1] and wholeBoard[0][0] == " x ") and wholeBoard[0][1] == "   ":
        wholeBoard[0][1] = " x "
    elif (wholeBoard[1][0] == wholeBoard[1][1] and wholeBoard[1][0] == " x ") and wholeBoard[1][1] == "   ":
        wholeBoard[1][1] = " x "
    elif (wholeBoard[2][0] == wholeBoard[2][1] and wholeBoard[2][0] == " x ") and wholeBoard[2][1] == "   ":
        wholeBoard[2][1] = " x "
    elif (wholeBoard[0][0] == wholeBoard[1][0] and wholeBoard[0][0] == " x ") and wholeBoard[1][0] == "   ":
        wholeBoard[1][0] = " x "
    elif (wholeBoard[0][1] == wholeBoard[1][1] and wholeBoard[0][1] == " x ") and wholeBoard[1][1] == "   ":
        wholeBoard[1][1] = " x "
    elif (wholeBoard[0][2] == wholeBoard[1][2] and wholeBoard[0][2] == " x ") and wholeBoard[1][2] == "   ":
        wholeBoard[1][2] = " x "
    elif (wholeBoard[0][0] == wholeBoard[1][1] and wholeBoard[0][0] == " x ") and wholeBoard[2][2] == "   ":
        wholeBoard[2][2] = " x "
    elif (wholeBoard[0][2] == wholeBoard[1][1] and wholeBoard[0][2] == " x ") and wholeBoard[2][0] == "   ":
        wholeBoard[2][0] = " x "
    #first 2 in row c
    elif (wholeBoard[0][0] == wholeBoard[0][1] and wholeBoard[0][0] == " o ") and wholeBoard[0][1] == "   ":
        wholeBoard[0][1] = " x "
    elif (wholeBoard[1][0] == wholeBoard[1][1] and wholeBoard[1][0] == " o ") and wholeBoard[1][1] == "   ":
        wholeBoard[1][1] = " x "
    elif (wholeBoard[2][0] == wholeBoard[2][1] and wholeBoard[2][0] == " o ") and wholeBoard[2][1] == "   ":
        wholeBoard[2][1] = " x "
    elif (wholeBoard[0][0] == wholeBoard[1][0] and wholeBoard[0][0] == " o ") and wholeBoard[1][0] == "   ":
        wholeBoard[1][0] = " x "
    elif (wholeBoard[0][1] == wholeBoard[1][1] and wholeBoard[0][1] == " o ") and wholeBoard[1][1] == "   ":
        wholeBoard[1][1] = " x "
    elif (wholeBoard[0][2] == wholeBoard[1][2] and wholeBoard[0][2] == " o ") and wholeBoard[1][2] == "   ":
        wholeBoard[1][2] = " x "
    elif (wholeBoard[0][0] == wholeBoard[1][1] and wholeBoard[0][0] == " o ") and wholeBoard[2][2] == "   ":
        wholeBoard[2][2] = " x "
    elif (wholeBoard[0][2] == wholeBoard[1][1] and wholeBoard[0][2] == " o ") and wholeBoard[2][0] == "   ":
        wholeBoard[2][0] = " x "
    # last 2 in row x
    elif (wholeBoard[0][1] == wholeBoard[0][2] and wholeBoard[0][1] == " x ") and wholeBoard[0][0] == "   ":
        wholeBoard[0][0] = " x "
    elif (wholeBoard[1][1] == wholeBoard[1][2] and wholeBoard[1][1] == " x ") and wholeBoard[1][0] == "   ":
        wholeBoard[1][0] = " x "
    elif (wholeBoard[2][1] == wholeBoard[2][2] and wholeBoard[2][1] == " x ") and wholeBoard[2][0] == "   ":
        wholeBoard[2][0] = " x "
    elif (wholeBoard[2][0] == wholeBoard[1][0] and wholeBoard[2][0] == " x ") and wholeBoard[0][0] == "   ":
        wholeBoard[0][0] = " x "
    elif (wholeBoard[2][1] == wholeBoard[1][1] and wholeBoard[2][1] == " x ") and wholeBoard[0][1] == "   ":
        wholeBoard[0][1] = " x "
    elif (wholeBoard[2][2] == wholeBoard[1][2] and wholeBoard[2][2] == " x ") and wholeBoard[0][2] == "   ":
        wholeBoard[0][2] = " x "
    elif (wholeBoard[2][2] == wholeBoard[1][1] and wholeBoard[2][2] == " x ") and wholeBoard[0][0] == "   ":
        wholeBoard[0][0] = " x "
    elif (wholeBoard[2][0] == wholeBoard[1][1] and wholeBoard[2][0] == " x ") and wholeBoard[0][2] == "   ":
        wholeBoard[0][2] = " x "
    #last 2 in row o
    elif (wholeBoard[0][1] == wholeBoard[0][2] and wholeBoard[0][1] == " o ") and wholeBoard[0][0] == "   ":
        wholeBoard[0][0] = " x "
    elif (wholeBoard[1][1] == wholeBoard[1][2] and wholeBoard[1][1] == " o ") and wholeBoard[1][0] == "   ":
        wholeBoard[1][0] = " x "
    elif (wholeBoard[2][1] == wholeBoard[2][2] and wholeBoard[2][1] == " o ") and wholeBoard[2][0] == "   ":
        wholeBoard[2][0] = " x "
    elif (wholeBoard[2][0] == wholeBoard[1][0] and wholeBoard[2][0] == " o ") and wholeBoard[0][0] == "   ":
        wholeBoard[0][0] = " x "
    elif (wholeBoard[2][1] == wholeBoard[1][1] and wholeBoard[2][1] == " o ") and wholeBoard[0][1] == "   ":
        wholeBoard[0][1] = " x "
    elif (wholeBoard[2][2] == wholeBoard[1][2] and wholeBoard[2][2] == " o ") and wholeBoard[0][2] == "   ":
        wholeBoard[0][2] = " x "
    elif (wholeBoard[2][2] == wholeBoard[1][1] and wholeBoard[2][2] == " o ") and wholeBoard[0][0] == "   ":
        wholeBoard[0][0] = " x "
    elif (wholeBoard[2][0] == wholeBoard[1][1] and wholeBoard[2][0] == " o ") and wholeBoard[0][2] == "   ":
        wholeBoard[0][2] = " x "
    else:
        print("Randomelse")
        i = rand.randint(0, len(wholeBoard)-1)
        j = rand.randint(0, len(wholeBoard[i])-1)
        if wholeBoard[i][j] == "   ":
            wholeBoard[i][j] = " x "
        else:
            while (wholeBoard[i][j] != "   "):
                i = rand.randint(0, len(wholeBoard)-1)
                j = rand.randint(0, len(wholeBoard[i])-1)
            wholeBoard[i][j] = " x "
    return wholeBoard
def printBoard(wholeBoard):
    for i in range(0,len(wholeBoard)):
        for j in range(0,len(wholeBoard[i])):
            if (j == len(wholeBoard[i])-1):
                print(wholeBoard[i][j])
                if (i != len(wholeBoard)-1):
                    print("-----------")
            else:
                print(wholeBoard[i][j] + "|",end="")
    print("\n\n")

def isGameOver(wholeBoard):
    gameOver = False
    '''for i in range(0,len(wholeBoard)):
        if wholeBoard[i][0] == wholeBoard[i][1] and  wholeBoard[i][0] == wholeBoard[i][2] and wholeBoard[i][0] != "   ":
            gameOver = True
    return gameOver'''
    if (wholeBoard[0][0] == wholeBoard[0][2] and wholeBoard[0][0] == wholeBoard[0][1]) and wholeBoard[0][1] == " x ":
        gameOver = True
    elif (wholeBoard[1][0] == wholeBoard[1][2] and wholeBoard[1][0] ==  wholeBoard[1][1]) and wholeBoard[1][1] == " x ":
        gameOver = True
    elif (wholeBoard[2][0] == wholeBoard[2][2] and wholeBoard[2][0] == wholeBoard[2][1]) and wholeBoard[2][1] == " x ":
        gameOver = True
    elif (wholeBoard[0][0] == wholeBoard[2][0] and wholeBoard[0][0] == wholeBoard[1][0]) and wholeBoard[1][0] == " x ":
        gameOver = True
    elif (wholeBoard[0][1] == wholeBoard[2][1] and wholeBoard[0][1] == wholeBoard[1][1]) and wholeBoard[1][1] == " x ":
        gameOver = True
    elif (wholeBoard[0][2] == wholeBoard[2][2] and wholeBoard[0][2] == wholeBoard[1][2]) and wholeBoard[1][2] == " x ":
        gameOver = True
    elif (wholeBoard[0][0] == wholeBoard[2][2] and wholeBoard[0][0] == wholeBoard[1][1]) and wholeBoard[1][1] == " x ":
        gameOver = True
    elif (wholeBoard[0][2] == wholeBoard[2][0] and wholeBoard[0][2] == wholeBoard[1][1]) and wholeBoard[1][1] == " x ":
        gameOver = True

    #for o
    if (wholeBoard[0][0] == wholeBoard[0][2] and wholeBoard[0][0] == wholeBoard[0][1]) and wholeBoard[0][1] == " o ":
        gameOver = True
    elif (wholeBoard[1][0] == wholeBoard[1][2] and wholeBoard[1][0] ==  wholeBoard[1][1]) and wholeBoard[1][1] == " o ":
        gameOver = True
    elif (wholeBoard[2][0] == wholeBoard[2][2] and wholeBoard[2][0] == wholeBoard[2][1]) and wholeBoard[2][1] == " o ":
        gameOver = True
    elif (wholeBoard[0][0] == wholeBoard[2][0] and wholeBoard[0][0] == wholeBoard[1][0]) and wholeBoard[1][0] == " o ":
        gameOver = True
    elif (wholeBoard[0][1] == wholeBoard[2][1] and wholeBoard[0][1] == wholeBoard[1][1]) and wholeBoard[1][1] == " o ":
        gameOver = True
    elif (wholeBoard[0][2] == wholeBoard[2][2] and wholeBoard[0][2] == wholeBoard[1][2]) and wholeBoard[1][2] == " o ":
        gameOver = True
    elif (wholeBoard[0][0] == wholeBoard[2][2] and wholeBoard[0][0] == wholeBoard[1][1]) and wholeBoard[1][1] == " o ":
        gameOver = True
    elif (wholeBoard[0][2] == wholeBoard[2][0] and wholeBoard[0][2] == wholeBoard[1][1]) and wholeBoard[1][1] == " o ":
        gameOver = True
    return gameOver

def isBoardFilled(wholeBoard):
    boardFilled = True
    for i in range(0,len(wholeBoard)):
        for j in range(0,len(wholeBoard[i])):
            if (wholeBoard[i][j]=="   "):
                boardFilled = False
    return boardFilled

#run with no parameters to start a game
def game():
    row1 = ["   ", "   ", "   "]
    row3 = ["   ", "   ", "   "]
    row5 = ["   ", "   ", "   "]
    wholeBoard = [row1, row3, row5]
    playerMove = 1
    aIMove = 1
    gameOver = False
    printBoard(wholeBoard)
    winner = ""
    while gameOver == False:
        printBoard(wholeBoard)
        wholeBoard = aITurn(wholeBoard,aIMove)
        printBoard(wholeBoard)
        if isGameOver(wholeBoard) == True:
            printBoard(wholeBoard)
            winner = "AI"
            break
        if (isBoardFilled(wholeBoard)) == True and isGameOver(wholeBoard) == False:
            winner = "Nobody"
            break
        aIMove += 1
        wholeBoard = playerTurn(wholeBoard)
        if isGameOver(wholeBoard) == True:
            printBoard(wholeBoard)
            winner = "Player"
            break
        printBoard(wholeBoard)
        playerMove += 1
        if (isBoardFilled(wholeBoard)) == True and isGameOver(wholeBoard) == False:
            winner = "Nobody"
            break
    print("Game Over!!!",winner,"wins!")



playAgain = "y"
while playAgain != "n":
    game()
    playAgain = input("Enter y to play again and n to stop playing:")




