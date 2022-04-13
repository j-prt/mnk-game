import graphics, os, re
from classes import Board, Player

#Function definitions

def clear():
    """Clears terminal. To be used between games"""

    os.system('cls' if os.name=='nt' else 'clear')

def start_game():
    """Prompts user to input desired board size and streak length and craft an m,n,k style game of their liking"""

    print(graphics.title)
    print('\n\n')
    game_selection = input("Welcome to Tic-Tac-Oh! What size board do you want? Width x Height: ")
    if game_selection == 'quit':
        quit()

    dimensions = [int(n) for n in re.split('\D', game_selection) if n.isdigit()]
    if len(dimensions) != 2:
        dimensions = [int(n) for n in re.split('\D', input("Please input two values ")) if n.isdigit()]
    while dimensions[0] not in list(range(3, 16)) or dimensions[1] not in (range(3, 16)):
        dimensions = [int(n) for n in re.split('\D', input("Please input values from 3 to 15 ")) if n.isdigit()]
    select_k = int(input("Streak length? "))
    while select_k not in list(range(3, 16)):
        select_k = int(input("Please input a number from 3 to 15 "))
    return Board(dimensions[0], dimensions[1], select_k)

def new_player(board, x_o):
    """Instantiate a player"""

    name = input(f"Input Player {x_o} name: " )
    return Player(name, x_o, board)

# Call functions to create board and player,
#  set counter toggle variable for turn switching 
# and set game_engine variable to control the main game loop

board = start_game()
p1 = new_player(board, 1)
p2 = new_player(board, 2)
game_engine = True
counter = 0

while game_engine == True:

    # Set game_on variable to control the round loop, 
    # clear the title screen and print a new game board

    board.game_on = True
    clear()
    print(graphics.battle)
    board.draw_board()
    while board.game_on:

        # Toggles player turns using bitwise NOT
        counter = ~counter
        if counter:
            p1.place()
        else:
            p2.place()

        # Checks winning conditions for each player,
        # checks if board is in draw state,
        # and prints game end flavour text

        if board.win(p1):
            print(f'{p1.name} is the... \n\n\n {graphics.winner}')
            board.game_end()
        elif board.win(p2):
            print(f'{p2.name} is the... \n\n\n {graphics.winner}')
            board.game_end()
        if board.draw():
            print(f'{graphics.draw}\n\nWell.. isn\'t that disappointing?')
            board.game_end()

    # Prompts players to play again or quit. 
    # Final score is displayed on quit and is a mystery until then!

    again = input("Keep playing? Y/N ").lower()
    while again not in ['y', 'n']:
        again = input("Keep playing? Y/N ").lower()
    if again == 'y':
        continue
    elif again == 'n':
        game_engine == False
        input(f"Score: \n{p1.name}: {p1.score} \n{p2.name}: {p2.score}\n\n\nThanks for playing!")
        quit()