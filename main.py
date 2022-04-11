from classes import Board, Player


# VALS = ["_", "X", "O"]
# COLS = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "O"]
# ROWS = iter(list(range(1, 16)))
# board = [[0 for n in range(3)] for i in list(range(3))]

# board_drawn = "    "
# for n in range(len(board[0])):
#     board_drawn += f" {COLS[n]}  "   
# for row in board:
#     board_drawn += f"\n{next(ROWS):2} "
#     for item in row:   
#         board_drawn += f"| {VALS[item]} "
#     board_drawn += "|"





# print(board[0] == board)
# print

board = Board(3,3,3)
board.draw_board()

p1 = Player(1, board)

p1.place("A1")

board.draw_board()

#check three things: 
#one - the horizontal (within the rows)
#two - the vertical (same index across rows)
#three - the diagonal (sequential indices across rows)
#only needs to check current move  
#track movelist 