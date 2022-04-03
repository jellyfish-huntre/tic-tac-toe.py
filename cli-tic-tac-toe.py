import math

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
# list(range(1, 10))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def main():
    player = 'x'
    printBoard()
    winner = whoWon()
    while winner == None:
        move(player)
        if player == 'o':
            player = 'x'
        else:
            player = 'o'
        winner = whoWon()

    if winner != 'draw':
        print(winner + ' wins!')
    else:
        print('Draw!')


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


def whoWon():
    # for row in board:
    #     if row[0] != ' ' and row[0] == row[1] and row[1] == row[2]:
    #         return row[0]

    tiles = []

    for row in board:
        for tile in row:
            tiles.append(tile)

    winningPatterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
        0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for pattern in winningPatterns:
        if tiles[pattern[0]] != ' ' and tiles[pattern[0]] == tiles[pattern[1]] and tiles[pattern[1]] == tiles[pattern[2]]:
            return tiles[pattern[0]]

    if isFull():
        return 'draw'
    return None


def isFull():
    for row in board:
        for tile in row:
            if tile == ' ':
                return False
    return True


main()
