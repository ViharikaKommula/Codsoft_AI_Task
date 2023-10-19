import tkinter as tk
from tkinter import messagebox
class TicTacToe:
    def __init__(self, game_modes, rounds, dark_mode):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.dark_mode = dark_mode
        if self.dark_mode:
            self.window.configure(bg='#2C3E50')
        self.game_modes = game_modes
        self.rounds = rounds
        self.results = []
        self.buttons = [[None for i in range(3)] for j in range(3)]
        self.current_round = 1
        self.current_player = "X"
        self.create_buttons()
    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text="", font=("Helvetica", 20), width=6, height=2,
                                               command=lambda row=i, col=j: self.on_click(row, col))
                if self.dark_mode:
                    self.buttons[i][j].configure(bg='#34495E', fg='#ECF0F1')
                self.buttons[i][j].grid(row=i, column=j)
    def on_click(self, row, col):
        if self.buttons[row][col]["text"] == "":
            self.buttons[row][col]["text"] = self.current_player
            if self.check_win(row, col):
                self.results.append(f"Player {self.current_player} wins Round {self.current_round}")
                self.current_round += 1
                self.restart_game()
            elif self.check_draw():
                self.results.append("It's a draw!")
                self.current_round += 1
                self.restart_game()
            else:
                if self.game_modes == "Player vs AI" and self.current_round <= self.rounds:
                    self.ai_move()
                elif self.game_modes == "Player vs Player" and self.current_round <= self.rounds:
                    self.current_player = "O" if self.current_player == "X" else "X"
                elif self.current_round > self.rounds:
                    self.display_game_result()
    def ai_move(self):
        best_score = float('-inf')
        move = None
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] == "":
                    self.buttons[i][j]["text"] = "O"
                    score = self.minimax(0, False, float('-inf'), float('inf'))
                    self.buttons[i][j]["text"] = ""
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        if move:
            self.buttons[move[0]][move[1]]["text"] = "O"
            if self.check_win(move[0], move[1]):
                self.results.append("AI Wins!")
                self.current_round += 1
                self.restart_game()
            elif self.check_draw():
                self.results.append("It's a draw!")
                self.current_round += 1
                self.restart_game()
            else:
                self.current_player = "X"
    def minimax(self, depth, is_maximizing, alpha, beta):
        if self.check_win():
            return -1 if is_maximizing else 1
        elif self.check_draw():
            return 0
        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.buttons[i][j]["text"] == "":
                        self.buttons[i][j]["text"] = "O"
                        score = self.minimax(depth + 1, False, alpha, beta)
                        self.buttons[i][j]["text"] = ""
                        best_score = max(score, best_score)
                        alpha = max(alpha, best_score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.buttons[i][j]["text"] == "":
                        self.buttons[i][j]["text"] = "X"
                        score = self.minimax(depth + 1, True, alpha, beta)
                        self.buttons[i][j]["text"] = ""
                        best_score = min(score, best_score)
                        beta = min(beta, best_score)
                        if beta <= alpha:
                            break
            return best_score
    def check_win(self, row=None, col=None):
        if row is not None and col is not None:
            return self.check_row(row) or self.check_column(col) or self.check_diagonal(row, col)
        else:
            return any(self.check_row(i) or self.check_column(i) for i in range(3)) or \
                   any(self.check_diagonal(i, j) for i in range(3) for j in range(3))
    def check_row(self, row):
        return self.buttons[row][0]["text"] == self.buttons[row][1]["text"] == self.buttons[row][2]["text"] != ""
    def check_column(self, col):
        return self.buttons[0][col]["text"] == self.buttons[1][col]["text"] == self.buttons[2][col]["text"] != ""
    def check_diagonal(self, row, col):
        if row == col:
            return self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != ""
        elif row + col == 2:
            return self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != ""
        return False
    def check_draw(self):
        return all(self.buttons[i][j]["text"] != "" for i in range(3) for j in range(3))
    def restart_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
        if self.game_modes == "Player vs AI" and self.current_round <= self.rounds:
            self.ai_move()
        elif self.game_modes == "Player vs Player" and self.current_round <= self.rounds:
            self.current_player = "O" if self.current_player == "X" else "X"
        elif self.current_round > self.rounds:
            self.display_game_result()
    def display_game_result(self):
        result_message = "\n".join(self.results)
        messagebox.showinfo("Game Over", f"All rounds completed. Game Over!\n\n{result_message}")
        self.window.destroy()
    def run(self):
        self.window.mainloop()
def choose_game_modes():
    game_modes = var.get()
    root.destroy()
    choose_rounds(game_modes)
def choose_rounds(game_modes):
    rounds = var2.get()
    dark_mode = var3.get()
    game = TicTacToe(game_modes, rounds, dark_mode)
    game.run()
root = tk.Tk()
root.title("Tic-Tac-Toe Setup")
var = tk.StringVar(root)
var.set("Player vs AI")
var2 = tk.IntVar(root)
var2.set(3)
var3 = tk.BooleanVar(root)
var3.set(False)
label = tk.Label(root, text="Select Game Mode:")
label.pack()
modes = tk.OptionMenu(root, var, "Player vs AI", "Player vs Player")
modes.pack()
label2 = tk.Label(root, text="Select Number of Rounds:")
label2.pack()
rounds = tk.OptionMenu(root, var2, 3, 5)
rounds.pack()
label3 = tk.Label(root, text="Dark Mode:")
label3.pack()
dark_mode_checkbox = tk.Checkbutton(root, variable=var3)
dark_mode_checkbox.pack()
button = tk.Button(root, text="Generate Game", command=choose_game_modes)
button.pack()
root.mainloop()