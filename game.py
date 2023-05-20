from board import Board
import math
import time
import alphabeta

def main():
    board = Board()
    time.sleep(3)
    game_end = False
    AI = True
    while not game_end:
        (game_board, game_end) = board.get_game_grid()
        board.print_grid(game_board)

        if AI:
            col = alphabeta.alplhaBeta(True,5,game_board, -math.inf, math.inf)[0]
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
    main()
