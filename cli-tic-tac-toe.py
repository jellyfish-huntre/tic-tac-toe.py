import math

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
moves = list(range(1, 10))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


def main():
    player = 'x'
    for i in range(9):
        move(player)
        if player == 'o':
            player = 'x'
        else:
            player = 'o'


def printBoard():
    for row in board:
        print(row[0] + ' | ' + row[1] + ' | ' + row[2])
        if board[2] is not row:
            print('--+---+--')


def promptUser(prompt: str, errorPrompt: str, choices: list, responseType=str):
    userInput = responseType(input(prompt))
    while (userInput not in choices):
        userInput = responseType(input(errorPrompt))

    return userInput


def move(player: str):
    print(player + "'s turn")
    move = promptUser("What is your move? (1-9) ",
                      "Please enter an integer between 1 and 9 that has not been taken: ", moves, int)
    moves.remove(move)
    changeBoard(move, player)


def changeBoard(move, player):
    move -= 1
    row = math.floor(move/3)
    tile = move % 3
    board[row][tile] = player
    printBoard()


def gameOver():
    pass


main()
