
class Game:
    def __init__(self):
        self.turnNum = 0
        self.winner = None
        self.board = [[" "," "," "],[" ", " ", " "],[" ", " ", " "]]

    def drawBoard(self):  # draws the board one row at a time
        for row in range(len(self.board)):
            if row == 0:  # special case, allows me to print the column numbers
                print "  " + "1 " + "2 " + "3 "
            print str(row+1),  # print the row numbers
            for square in range(3):
                print str(self.board[row][square]),  # print the item in that row
            print ""

    def setSquare(self, row, column, value):
        self.board[row][column] = value

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
        self.turnNum += 1
        self.drawBoard()



"""class Bot:
    def __init__(self, team, game):
        self.team = team
        self.moves = {} #this dictionary will hold the optimal move in each scenario
        self.game = game
    def move(self):
        try:
            movesList = self.moves[self.game.getGameState()]
            highestValue = 0;"""

test = Game()  # for testing purposes

