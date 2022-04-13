"""Defines classes to be used in m,n,k-style game."""


VALS = ["_", "X", "O"]
COLS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]


class Board:
    """Maintains and draws the state of the game board as well as win/lose conditions"""

    def __init__(self, m, n, k=4):
        """m denotes board width (rows), n denotes height (columns), k denotes required streak for a win"""
        self.m = m
        self.n = n
        self.k = k
        self.board = [[0 for row in range(self.m)] for col in list(range(self.n))]
        self.game_on = False
        self.players = []
        self.moves = 0
        self.max_moves = m * n
        
    def new_board(self):
        self.moves = 0
        self.board = [[0 for row in range(self.m)] for col in list(range(self.n))]

    def draw_board(self):
        """Draws the game board based on board data"""
        board_drawn = "    "
        for n in range(len(self.board[0])):
            board_drawn += f" {COLS[n]}  "   
        for index, row in enumerate(self.board):
            board_drawn += f"\n{index+1:2} "
            for item in row:   
                board_drawn += f"| {VALS[item]} "
            board_drawn += "|"
        print(board_drawn)

    def win(self, player):
        """Identifies if the game is in a winning state"""

        #Original function for checking a diagonal win scenario
        # for row_index, row in enumerate(self.board):
        #     for col_index, num in enumerate(row):
        #         try:
        #             if num == 0:
        #                 continue
        #             elif self.board[row_index+1][col_index+1] == num and self.board[row_index-1][col_index-1] == num:
        #                 if row_index-1 < 0 or col_index-1 < 0:
        #                     continue
        #                 print('diagonal1')
        #                 player.score += 1
        #                 return True
        #             elif self.board[row_index-1][col_index+1] == num and self.board[row_index+1][col_index-1] == num:
        #                 if row_index-1 < 0 or col_index-1 < 0:
        #                     continue
        #                 print('diagonal2')
        #                 player.score += 1
        #                 return True
        #         except:
        #             continue
                
        #Updated diagonal win checker
        for row_index, row in enumerate(self.board):
            for item_index, item in enumerate(row[:-self.k+1]):
                count_to_kd_pos = 1
                count_to_kd_neg = 1
                if item != player.player:
                    continue
                item_index_pos = item_index
                item_index_neg = item_index
                row_index_pos = row_index
                row_index_neg = row_index
                for i in range(self.k):
                    try:
                        if item == self.board[row_index_pos+1][item_index_pos+1]:
                            count_to_kd_pos += 1
                            item_index_pos += 1
                            row_index_pos += 1
                    except:
                        pass
                    try:
                        if item == self.board[row_index_neg-1][item_index_neg+1]:
                            item_index_neg += 1
                            row_index_neg -= 1
                            count_to_kd_neg += 1
                    except:
                        pass
                    if count_to_kd_pos == self.k or count_to_kd_neg == self.k:
                        player.score += 1
                        return True
                    pass
        

        #Check horizontal win
        for row in self.board:
            count_to_k = 1
            for i in range(self.m-1):
                if row[i] == row[i+1] and row[i] == player.player:
                    count_to_k += 1
                else:
                    count_to_k = 1
                if count_to_k == self.k:
                    player.score += 1
                    return True
                else:
                    continue


        #Check vertical win
        for alpha, column in player.moves.items():
            column = sorted(list(column))
            count_to_kv = 1
            for item in column:
                try:
                    if item + 1 == column[column.index(item)+1]:
                        count_to_kv +=1
                    else:
                        count_to_kv = 1
                except:
                    count_to_kv = 1
                if count_to_kv == self.k:
                    player.score += 1
                    return True
            return False

    def draw(self):
        if self.moves == self.max_moves:
            return True
        else:
            return False

    def game_end(self):
        """Updates the board with players' move, calls draw_board and game_end"""
        self.players[0].moves = {}
        self.players[1].moves = {}
        self.moves = 0
        self.game_on = False
        self.new_board()




class Player:
    """Contains basic player information and actions"""

    def __init__(self, name=str, player=int, game_board=None):
        self.player = player
        self.name = name
        self.moves = {}
        self.score = 0
        self.game_board = game_board
        self.game_board.players.append(self)

    def place(self):
        """Add a marker to the board. Coordinate received as tuple from user input"""
        coord = input(f'{self.name}, your move: ').upper()
        if coord == "FORFEIT":
            self.forfeit()
            return None

        try:
            alpha, num = coord[0], int(coord[1:])-1
            while self.game_board.board[num][COLS.index(alpha)] != 0 or len(coord) >3:
                coord = input('Please play a valid move: ').upper()
                alpha, num = list(coord)[0], int(list(coord)[1])-1
            self.game_board.board[num][COLS.index(alpha)] = self.player
            self.game_board.moves +=1
            self.game_board.draw_board()
            try:
                self.moves[alpha] += [num]
            except:
                self.moves[alpha] = [num]
        except:
            input('Invalid entry... ')
            self.place()
        

    def forfeit(self):
        """Concede the game"""
        input(f"{self.name} has forfeitted the game.")
        self.game_board.players[self.player-2].score += 1
        self.game_board.game_end()

#TODO - code the AI opponent
class Com(Player):
    """AI ("COM") player to play against a player in single-player mode"""

    def __init__(self):
        super.__init__()

    def place(self):
        #coordinate should be based on picking next available adjacency to longest streak
        pass