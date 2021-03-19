# Graphics driver for game.py.
# code inspired by link below
# https://www.geeksforgeeks.org/tic-tac-toe-gui-in-python-using-pygame/


import pygame as pg 
import sys 
import time 
from pygame.locals import *

width = 400
height = 400 # w x h values for the game window
white = (255, 255, 255) # for background
line_color = (0, 0, 0) # black value for lines that will divide the board

pg.init()

fps = 30

CLOCK = pg.time.Clock()

x_img = pg.image.load("x_picture.png")
o_img = pg.image.load("o_picture.png")

screen = pg.display.set_mode((width, height), 0, 32)
pg.display.set_caption("TTT")


def init_screen(m, n): # where m is rows and n is columns
    screen.fill(white)
    global x_img
    global o_img
    x_img = pg.transform.scale(x_img, (int(width / n) - 20, int(height / m) - 20))
    o_img = pg.transform.scale(o_img, (int(width / n) - 20, int(height / m) - 20))
    # vertical lines - divide by n, do this n-1 times.
    for i in range(n - 1):
        pg.draw.line(screen, line_color, (width / n * (i + 1), 0), (width / n * (i + 1), height), 3)
    # horizontal lines - divide by m, do m-1 times.
    for j in range(m - 1):
        pg.draw.line(screen, line_color, (0, height / m * (j + 1)), (width, height / m * (j + 1)), 3)
    pg.display.update()
    time.sleep(1)
    

def update_screen(x, y, move):#(board, m, n, move):
    if(move == 'X'):
        screen.blit(x_img, (x + 20, y + 20))
    else:
        screen.blit(o_img, (x + 20, y + 20))
    pg.display.update()

# handles drawing the turn on the board, changing
# the turn from X->O or vice versa
def user_click(board, m, n, move):
    #print(move, "-----")
    #print(board)
    x, y = pg.mouse.get_pos()
    row = 0
    col = 0
    for i in range(n):
        if(x < int(width / n * (i + 1))):
            col = i
            #print(col)
            break
    for j in range(m):
        if(y < int(height / m * (j + 1))):
            row = j
            #print(row)
            break
    if(board[row][col] == ' '):
        board[row][col] = move
        update_screen(col * width / n, row * height / m, move)
        return True
    return False

#def win_screen():

#def tie_screen():

  