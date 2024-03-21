from tkinter import *
from tkinter import messagebox
from game_logic.computer_play import ComputerPlayer


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.board = [[" " for i in range(3)] for j in range(3)]
        self.buttons = [[Button(master, text=" ", font=("Helvetica", 20), width=4, height=2,
                                command=lambda x=i, y=j: self.play(x, y))
                        for j in range(3)] for i in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)
        self.turn = "X"
        self.message = Label(master, text="Turno de : X", font=("Helvetica", 20))
        self.message.grid(row=3, column=0, columnspan=3)
        self.game_over = False
        self.computer_player = ComputerPlayer(self)

    def play(self, x, y):
        if self.board[x][y] == " " and not self.game_over:
            self.board[x][y] = self.turn
            color = "blue" if self.turn == "X" else "red"
            self.buttons[x][y].config(text=self.turn, fg=color)
            if self.check_winner():
                self.message.config(text=f"¡{self.turn} Ganó!")
                self.game_over = True
            elif self.check_tie():
                self.message.config(text="¡Empate!")
                self.game_over = True
            else:
                self.turn = "O" if self.turn == "X" else "X"
                self.message.config(text=f"Turno de: {self.turn}")
                if self.turn == "O":
                    self.computer_play()

    def computer_play(self):
        x, y = self.computer_player.get_best_move()
        self.play(x, y)

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != ' ':
                self.end_game(self.buttons[i][0]['text'])
        for i in range(3):
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != ' ':
                self.end_game(self.buttons[0][i]['text'])
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != ' ':
            self.end_game(self.buttons[0][0]['text'])
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != ' ':
            self.end_game(self.buttons[0][2]['text'])
        if self.check_tie():
            self.end_game('tie')

    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]['text'] == ' ':
                    return False
        return True

    def end_game(self, winner):
        self.game_over = True
        if winner == 'tie':
            message = "¡Empate!"
        else:
            message = f"¡{winner} ganó!"
        self.message.config(text=message)
        play_again = messagebox.askyesno("Juega otra vez", "¿Quieres jugar de nuevo?")
        if play_again:
            self.board = [[" " for i in range(3)] for j in range(3)]
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j].config(text=" ", fg="black")
            self.turn = "X"
            self.message.config(text="Turno de: X")
            self.game_over = False
        else:
            self.master.quit()