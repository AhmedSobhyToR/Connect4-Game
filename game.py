from board import Board
import math
import time
from tkinter import * 
import alphabeta

root = Tk()

root.title('Connect 4 - AI')



def main(depth):
    board = Board()
    time.sleep(3)
    game_end = False
    AI = True
    print('depth:' , depth)
    while not game_end:
        (game_board, game_end) = board.get_game_grid()
        board.print_grid(game_board)

        if AI:
            col = alphabeta.alplhaBeta(True,depth,game_board, -math.inf, math.inf)[0]
            if alphabeta.CorrectColumn(game_board, col):
                row = alphabeta.FirstMove(game_board, col)
                game_board[row][col] = alphabeta.PlayerType.AgentAI
                if alphabeta.hasWon(game_board, alphabeta.PlayerType.AgentAI):
                    print("Agent Won The Game")
                    board.select_column(col)
                    game_end = True

        board.select_column(col)
        time.sleep(2.5)


if __name__ == "__main__":

    frame = LabelFrame(root, padx = 20)
    easyButton = Button(frame, text = "Easy", padx = 20, pady = 20, command=lambda: main(4))
    mediumButton = Button(frame , text = "Medium",padx = 20, pady = 20, command=lambda: main(3))
    hardButton = Button(frame ,text = "Hard", padx = 20, pady = 20, command=lambda: main(5))
    frame.grid(row = 0, column = 0, padx = 30)
    easyButton.pack()

    for i in range(1):
        x = Label(frame)
        x.pack()
    mediumButton.pack()

    for i in range(1):
        x = Label(frame)
        x.pack()

    hardButton.pack()

    root.mainloop()
