
class Game:
    def __init__(self, playerX, playerO):
        self.turnNum = 0
        self.winner = None
        self.board = [[" "," "," "],[" ", " ", " "],[" ", " ", " "]] #(0,0) is top left
        self.recentSquare = None
        self.playerX = playerX
        self.playerO = playerO
    def drawBoard(self):  # draws the board one row at a time
        for row in range(len(self.board)):
            if row == 0:  # special case, allows me to print the column numbers
                print "  " + "1 " + "2 " + "3 "
            print str(row+1),  # print the row numbers
            for square in range(3):
                print str(self.board[row][square]),  # print the item in that row
            print ""
    def setSquare(self, row, column, value): # Y then X
        self.board[row][column] = value
    def getSquare(self, row, column): #Y then X
            return self.board[row][column]
    def turnPvp(self): #TIc-tac-toe for player - vs - player
        self.drawBoard()
        if self.turnNum % 2 == 0:
            currentTurnLetter = "x"
        else:
            currentTurnLetter = "o"
        print "It is " + currentTurnLetter + "'s turn"
        while True: #Making sure that the user's input is allowed by the rules
            while True:
                try:
                    userSelectionX = int(raw_input("Select Column. >> "))
                    userSelectionY = int(raw_input("Select Row. >>"))
                except ValueError:
                    print "Enter a valid number"
                    continue
                break
            if (userSelectionX > 3) or (userSelectionY > 3) or (userSelectionX <= 0) or (userSelectionY <= 0): #is the selection too large or too small?
                print "Enter a valid number"
                continue
            if self.getSquare(userSelectionY - 1, userSelectionX - 1) != " ":
                print "That square is occupied"
                continue
            else:
                break
        self.setSquare(userSelectionY-1, userSelectionX-1, currentTurnLetter)
        self.recentSquare = [userSelectionY-1, userSelectionX-1]
        self.turnNum += 1
    def turnPvb(self):
        self.drawBoard()
        if self.turnNum % 2 == 1: #Player's move, assuming player is O
            currentTurnLetter = "o"
            print "It is " + currentTurnLetter + "'s turn"
            while True:  # Making sure that the user's input is allowed by the rules
                while True:
                    try:
                        userSelectionX = int(raw_input("Select Column. >> "))
                        userSelectionY = int(raw_input("Select Row. >>"))
                    except ValueError:
                        print "Enter a valid number"
                        continue
                    break
                if (userSelectionX > 3) or (userSelectionY > 3) or (userSelectionX <= 0) or (
                        userSelectionY <= 0):  # is the selection too large or too small?
                    print "Enter a valid number"
                    continue
                if self.getSquare(userSelectionY - 1, userSelectionX - 1) != " ":
                    print "That square is occupied"
                    continue
                else:
                    break
        else: #Bot's move
            self.setSquare(self.playerX.getMove()[0], self.playerX.getMove()[1], "x")
            self.turnNum+=1
    def checkForWin(self):
        if self.recentSquare is None: #Just sanitizing input so this doesn't always crash on the first turn
            return None
        recentX = self.recentSquare[1]
        recentY = self.recentSquare[0]
        recentValue = self.getSquare(recentY, recentX)
        # Vertical Wins (Try-Catch is to avoid an index error when winning a different way)
        while True:
            try:
                if ((self.getSquare(recentY-1, recentX) == (recentValue)) and (self.getSquare(recentY-2, recentX) == (recentValue))): #3 in a row vertically from bottom
                    return True
                if ((self.getSquare(recentY-1, recentX) == (recentValue)) and (self.getSquare(recentY+1, recentX) == (recentValue))): #Vertically from middle
                    return True
                if ((self.getSquare(recentY+1, recentX) == (recentValue)) and (self.getSquare(recentY+2, recentX) == (recentValue))): #Vertically from top
                    return True
                break
            except IndexError:
                break

        #Horizontal Wins
        while True:
           try:
                if ((self.getSquare(recentY, recentX + 1) == (recentValue)) and (self.getSquare(recentY, recentX + 2) == (recentValue))): #Horizontally from top
                    return True
                if ((self.getSquare(recentY, recentX - 1) == (recentValue)) and (self.getSquare(recentY, recentX + 1) == (recentValue))):  # Horizontally from middle
                    return True
                if ((self.getSquare(recentY, recentX - 1) == (recentValue)) and (self.getSquare(recentY, recentX - 2) == (recentValue))):  # Horizontally from bottom
                    return True
                break
           except IndexError:
               break
        #Diagonal wins bottom to the right
        while True:
            try:
                if ((self.getSquare(recentY - 1, recentX + 1) == (recentValue)) and (self.getSquare(recentY - 2, recentX + 2) == (recentValue))): # Diagonally from bottom left
                    return True
                if ((self.getSquare(recentY - 1, recentX + 1) == (recentValue)) and (self.getSquare(recentY + 1, recentX - 1) == (recentValue))):  # Diagonally from middle going right up
                    return True
                if ((self.getSquare(recentY + 1, recentX - 1 ) == (recentValue)) and (self.getSquare(recentY + 2 , recentX - 2) == (recentValue))):  # Diagonally from top right
                    return True
                break
            except IndexError:
                break
        #Diagonal wins to the left
        while True:
            try:
                if ((self.getSquare(recentY - 1, recentX - 1 ) == (recentValue)) and (self.getSquare(recentY - 2 , recentX - 2) == (recentValue))):  # Diagonally from bottom right
                    return True
                if ((self.getSquare(recentY - 1, recentX - 1) == (recentValue)) and (self.getSquare(recentY + 1, recentX + 1) == (recentValue))):  # Diagonally from middle going left up
                    return True
                if ((self.getSquare(recentY + 1, recentX + 1) == (recentValue)) and (self.getSquare(recentY + 2, recentX + 2) == (recentValue))): # Diagonally from top left
                    return True
                break
            except IndexError:
                break
    def play(self):
        while self.checkForWin() is None:
            if isinstance(self.playerX, Bot):
                self.turnPvb()
            else:
                self.turnPvp()
        if self.turnNum % 2 == 0:
            print "O wins!"
        else:
            print "X wins!"


class Bot:
    def __init__(self, team, Game):
        self.team = team
        self.gameState = None
        self.moves = {}  # this dictionary will hold the optimal move in each scenario
    def getGameState(self, Game):
        self.gameState = Game.board
    def getMove(self):
        move = self.moves[self.gameState]



bot = Bot("x")
test = Game(bot, None)
test.play()

