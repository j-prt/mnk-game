"""Defines classes to be used in m,n,k-style game."""

VALS = ["_", "X", "O"]
COLS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]


class Board:
    """Maintains and draws the state of the game board as well as win/lose conditions"""

    def __init__(self, m, n, k):
        """m denotes board width (rows), n denotes height (columns), k denotes required streak for a win"""
        self.m = m
        self.n = n
        self.k = k
        self.board = [[0 for row in range(self.m)] for col in list(range(self.n))]
        self.players = []
        

    def draw_board(self):
        """Generates game board based on passed parameters"""
        board_drawn = "    "
        for n in range(len(self.board[0])):
            board_drawn += f" {COLS[n]}  "   
        for index, row in enumerate(self.board):
            board_drawn += f"\n{index+1:2} "
            for item in row:   
                board_drawn += f"| {VALS[item]} "
            board_drawn += "|"
        print(board_drawn)

    def game_end(self):
        """Identifies if the game is in a winning or draw state"""
        pass

    def update(self, player):
        """Updates the board with players' move, calls draw_board and game_end"""
        if len(player.moves) < self.k:
            pass
        else:
            pass
        pass


class Player:
    """Contains basic player information and actions"""

    def __init__(self, player=int, game_board=None):
        self.player = player
        self.moves = []
        self.score = 0
        self.game_board = game_board
        self.game_board.players.append(self)

    def place(self, coord):
        """Add a marker to the board. Coordinate received as tuple from user input"""
        alpha, num = list(coord)[0], int(list(coord)[1])-1
        self.game_board.board[num][COLS.index(alpha)] = self.player
        self.moves.append(coord)
        self.game_board.update(self)

    def forfeit(self):
        """Concede the game"""

class Com(Player):
    """AI ("COM") player to play against a player in single-player mode"""

    def __init__(self):
        super.__init__()

    def move(self):
        #coordinate should be based on picking next available adjacency to longest streak
        pass