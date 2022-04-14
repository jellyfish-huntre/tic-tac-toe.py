import math

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] # board of rows of tiles
moves = [1, 2, 3, 4, 5, 6, 7, 8, 9] # available moves

def main(): # main function, this is the equivalent of one tic-tac-toe game
    player = 'x'
    
    while whoWon(board) == None: # while the game has not ended
        move(player)
        if player == 'o':
            player = 'x'
        else:
            player = 'o'
    
    winner = whoWon(board)
    printBoard()
    if winner != 'draw':
        print(winner + ' wins!')
    else:
        print('Draw!')

def printBoard():
    '''prints the board as output'''
    for row in board:
        print(row[0] + ' | ' + row[1] + ' | ' + row[2])
        if board[2] is not row:
            print('--+---+--')


def promptUser(prompt: str, errorPrompt: str, choices: list, responseType=str):
    '''continously prompts the user until the user inputs an option. 
    Takes the original prompt, an error prompt, the choices, and the response type. Returns the input.'''
    userInput = input(prompt)
    try:
        userInput = responseType(userInput)
    except:
        pass
    while (userInput not in choices):
        userInput = input(errorPrompt)
        try:
            userInput = responseType(userInput)
        except:
            pass

    return userInput


def move(player: str):
    '''Takes the player as a parameter, prompts the user for their move, and changes the board'''
    print(player + "'s turn")
    printBoard()
    move = promptUser("What is your move? (1-9) ",
                      "Please enter a number between 1 and 9 that has not been taken: ", moves, int)
    moves.remove(move)
    changeBoard(move, player)


def changeBoard(move, player):
    '''accesses the board and changes one of the tiles. Takes a move and a player as parameters.'''
    move -= 1
    row = math.floor(move/3)
    tile = move % 3
    board[row][tile] = player
    print("\n")


def whoWon(board):
    '''Checks if the game is over, and returns draw or the player who won. 
    Returns none if the game is still ongoing.'''

    tiles = []

    for row in board:
        for tile in row:
            tiles.append(tile)

    winningPatterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
        0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for pattern in winningPatterns:
        if tiles[pattern[0]] != ' ' and tiles[pattern[0]] == tiles[pattern[1]] and tiles[pattern[1]] == tiles[pattern[2]]:
            return tiles[pattern[0]]

    if isFull(board):
        return 'draw'
    return None


def isFull(board):
    '''Checks each tile in the board and checks if they are empty. 
    If none are empty, return True. Else, return false.'''
    for row in board:
        for tile in row:
            if tile == ' ':
                return False
    return True


'''this is the mainloop. the user plays a game of tic tac toe and can choose to quit or play another, 
in which everything resets.'''

play = 'y'
print("Welcome to Tic-Tac-Toe!")

while play != 'n':
    main()
    play = promptUser('Would you like to play again? (y/n) ', "Please type 'y' or 'n': ", ['y', 'n'])
    print("\n")
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Thank you for playing!")
