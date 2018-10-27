
class Game:
    def __init__(self):
        self.turnNum = 0
        self.winner = None
        self.board = [[" "," "," "],[" ", " ", " "],[" ", " ", " "]]
        self.recentSquare = None
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
    def turn(self):
        self.drawBoard()
        if self.turnNum % 2 == 0:
            currentTurnLetter = "x"
        else:
            currentTurnLetter = "o"
        print "It is " + currentTurnLetter + "'s turn"
        while True:
            while True:
                try:
                    userSelectionX = int(raw_input("Select Column. >> "))
                    userSelectionY = int(raw_input("Select Row. >>"))
                    break
                except ValueError:
                    print "Enter a valid number"
            if (userSelectionX > 3) or (userSelectionY > 3):
                print "Enter a valid number"
            else:
                break
        self.setSquare(userSelectionY-1, userSelectionX-1, currentTurnLetter)
        self.recentSquare = [userSelectionY-1, userSelectionX-1]
        self.turnNum += 1
        self.drawBoard()
    def checkForWin(self):
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
           except IndexError:
               break
        #DIagonal Wins
        while True:
            try:
                if ((self.getSquare(recentY+1, recentX + 1) == (recentValue)) and (self.getSquare(recentY + 2, recentX + 2) == (recentValue))): # Diagonally from top
                    return True
                if ((self.getSquare(recentY - 1, recentX - 1) == (recentValue)) and (self.getSquare(recentY + 1, recentX + 1) == (recentValue))):  # Diagonally from middle
                    return True
                if ((self.getSquare(recentY - 1, recentX + 1 ) == (recentValue)) and (self.getSquare(recentY - 2 , recentX + 2) == (recentValue))):  # Diagonally from bottom
                    return True
            except IndexError:
                break



"""class Bot:
    def __init__(self, team, game):
        self.team = team
        self.moves = {} #this dictionary will hold the optimal move in each scenario
        self.game = game
    def move(self):
        try:
            movesList = self.moves[self.game.getGameState()]
            highestValue = 0;"""

test = Game()
test.turn()# for testing purposes
test.turn()
test.turn()
test.turn()
test.turn()
print test.checkForWin()
