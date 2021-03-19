
#Implementation of Two Player Tic-Tac-Toe game in Python.
# original source code: https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874
# edited by Joseph Tan

import graphicsTTT as gt

# generates a m x n 2D array and returns it
def generate_board(m, n):
    return ([[' ' for j in range(n)] for i in range(m)])

# win_indexes(n) and is_winner(board, decorator) found from StackOverflow 
# https://stackoverflow.com/questions/39922967/python-determine-tic-tac-toe-winner#:~:text=You%20can%20just%20make%20a,the%20game%20has%20been%20won.&text=This%20will%20return%20%22O%22%20if,%22%2C%20and%20%2D1%20otherwise.
# by Brendan Abel

def win_indexes(m,n):
    diff = abs(m-n)
    # print(diff)
    # Rows
    for r in range(m):
        yield [(r, c) for c in range(n)]
    # Columns
    for c in range(n):
        yield [(r, c) for r in range(m)]
    # Diagonal top left to bottom right
    for a in range(abs(m-n) + 1):
        x = [(i, i) for i in range(n)] if m == n else [(i, i+a) for i in range(n-diff)] if m < n else [(i+a, i) for i in range(n)] 
        yield x
    # Diagonal top right to bottom left
    for b in range(abs(m-n) + 1):
        y = [(i, n - 1 - i) for i in range(n)] if m == n else [(i, n - 1 - i - b) for i in range(n-diff)] if m < n else [(i+b, n - 1 - i) for i in range(n)] 
        yield y


def is_winner(board, decorator):
    m = len(board)
    n = len(board[0])
    for indexes in win_indexes(m,n):
        # print(indexes) # uncomment this to see all the indexes for solutions
        if all(board[r][c] == decorator for r, c in indexes):
            return True
    return False

def is_tie(board):
    tie = True
    for arr in board:
        if(any(x == ' ' for x in arr)):
            return False
    return tie
# ('-+'*len(board) + '-').join(['|'.join(board[row]) for row in range(len(board))])
def printBoard(board):
    print(('\n' + '+'.join(['-']*len(board[0])) + '\n').join(['|'.join(board[row]) for row in range(len(board))]))
 
# Now we'll write the main function which has all the gameplay functionality.
def game():
    theBoard = []
    win = False
    while True:
        print("Enter the grid you want for tic tac toe in this format: mxn")
        grid_specs = input().split('x') 
        m = int(grid_specs[0])
        n = int(grid_specs[1])
        if(m <= 0 or n <= 0):
            print("Invalid input. Try again.")
            continue
        else:
            theBoard = generate_board(int(grid_specs[0]), int(grid_specs[1]))
            break
    turn = 'X'
    gt.pg.init()
    gt.init_screen(m, n)
    # main loop
    while(True):
        for event in gt.pg.event.get():
            if event.type == gt.QUIT:
                gt.pg.quit()
                gt.sys.exit()
            elif event.type == gt.MOUSEBUTTONDOWN:
                if(gt.user_click(theBoard, m, n, turn)):
                    if(is_winner(theBoard, turn)):
                    # call winner display - print for now
                        win = True
                        print(turn + " is the winner")
                    if(turn == 'X'):
                        turn = 'O'
                    else:
                        turn = 'X'
        if(win):
            break
        elif(is_tie(theBoard)):
        # call tie display - print for now
            print("its a tie!")
            break
        gt.pg.display.update()
        gt.CLOCK.tick(gt.fps)     

if __name__ == "__main__":
    game()
