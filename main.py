class Square:
    def __init__(self, position, state):
        self.position = position # A tuple containing x and y coordiantes of the square, (0,0) being the upper left corner, and (2,2) being the lower right
        self.state = state # Either "x", "o" or 0.
    def setState(self, newState):
        self.state = newState
class Bot:
    def __init__(self, team, game):
        self.team = team
        self.moves = {} #this dictionary will hold the optimal move in each scenario
        self.game = game
    def move(self):
        try:
            movesList = self.moves[self.game.getGameState()]
            highestValue = 0;
            for move in movesList:

class Board:
    def __init__(self, squareList):
        self.containedSquares = squareList # Defining the squares on the board
    def reset(self):
        for square in self.containedSquares:
            square.setState(0)
class Game:
    turn = 0;
    def __init__(self, board):
        self.gameBoard = board
    def getGameState(self):
        return self.board.containedSquares


