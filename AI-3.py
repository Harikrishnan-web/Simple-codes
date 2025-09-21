import tkinter as tk
from tkinter import messagebox

HUMAN = 'X'
AI = 'O'
EMPTY = ''

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe with Alpha-Beta Pruning")
        self.board = [[EMPTY for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.game_over = False
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(
                    self.root, text='', font=('Arial', 32), width=5, height=2,
                    command=lambda x=i, y=j: self.player_move(x, y)
                )
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def player_move(self, x, y):
        if not self.game_over and self.board[x][y] == EMPTY:
            self.board[x][y] = HUMAN
            self.buttons[x][y]['text'] = HUMAN
            if self.check_winner(HUMAN):
                self.end_game("You Win!")
            elif self.is_draw():
                self.end_game("It's a Draw!")
            else:
                self.root.after(500, self.ai_move)

    def ai_move(self):
        best_score = float('-inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == EMPTY:
                    self.board[i][j] = AI
                    score = self.minimax(0, False, float('-inf'), float('inf'))
                    self.board[i][j] = EMPTY
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        if best_move:
            i, j = best_move
            self.board[i][j] = AI
            self.buttons[i][j]['text'] = AI
            if self.check_winner(AI):
                self.end_game("AI Wins!")
            elif self.is_draw():
                self.end_game("It's a Draw!")

    def minimax(self, depth, is_maximizing, alpha, beta):
        if self.check_winner(AI):
            return 10 - depth
        elif self.check_winner(HUMAN):
            return depth - 10
        elif self.is_draw():
            return 0
        if is_maximizing:
            max_eval = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == EMPTY:
                        self.board[i][j] = AI
                        eval = self.minimax(depth + 1, False, alpha, beta)
                        self.board[i][j] = EMPTY
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == EMPTY:
                        self.board[i][j] = HUMAN
                        eval = self.minimax(depth + 1, True, alpha, beta)
                        self.board[i][j] = EMPTY
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval

    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):
                return True
            if all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(self.board[i][j] != EMPTY for i in range(3) for j in range(3))

    def end_game(self, message):
        self.game_over = True
        messagebox.showinfo("Game Over", message)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
