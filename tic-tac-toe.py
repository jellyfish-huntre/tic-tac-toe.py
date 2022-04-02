import turtle

wn = turtle.Screen()
t = turtle.Turtle()

moves = [[0, 0], [0, 1], [0, 2], [1, 0], [
    1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
board = ['', '', '', '', '', '', '', '', '']


def tic_tac_toe():
    draw_board()


def draw_board():
    t.penup()
    t.goto(-150, 100)
    t.pendown()

    t.forward(300)

    t.penup()
    t.goto(-150, 200)
    t.pendown()

    t.forward(300)

    t.penup()
    t.goto(100, 0)
    t.pendown()

    t.left(90)
    t.forward(300)

    t.penup()
    t.goto(200, 0)
    t.pendown()

    t.forward(300)


def turn():
    pass


def reset():
    t.clear()
    draw_board(t)


tic_tac_toe()

wn.mainloop()
