from tkinter import *  
from tkinter import messagebox  
from game_logic.computer_play import ComputerPlayer  

class TicTacToe:  
    def __init__(self, master):  # Define el método de inicialización de la clase
        self.master = master  
        self.board = [[" " for i in range(3)] for j in range(3)]  # Inicializa el tablero del juego como una matriz vacía
        self.buttons = [[Button(master, text=" ", font=("Helvetica", 20), width=4, height=2,  # Crea una matriz de botones para representar el tablero
                                command=lambda x=i, y=j: self.play(x, y))  # Asigna la función play a cada botón con coordenadas (x, y)
                        for j in range(3)] for i in range(3)]
        for i in range(3):  # Coloca los botones en la ventana
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)
        self.turn = "X"  # Inicializa el turno del jugador como "X"
        self.message = Label(master, text="Turno de : X", font=("Helvetica", 20))  
        self.message.grid(row=3, column=0, columnspan=3)  
        self.game_over = False  # Inicializa el estado del juego como no terminado
        self.computer_player = ComputerPlayer(self)  # Crea una instancia de ComputerPlayer para permitir que la computadora juegue

    def play(self, x, y):  # Define el método para que el usuario realice un movimiento
        if self.board[x][y] == " " and not self.game_over:  
            self.board[x][y] = self.turn  # Actualiza el tablero con el movimiento del jugador
            color = "blue" if self.turn == "X" else "red"  
            self.buttons[x][y].config(text=self.turn, fg=color) 
            if self.check_winner():  # Verifica si hay un ganador después del movimiento
                self.message.config(text=f"¡{self.turn} Ganó!")  
                self.game_over = True 
            elif self.check_tie():  # Verifica si hay un empate después del movimiento
                self.message.config(text="¡Empate!")  
                self.game_over = True  
            else:  # Si el juego no ha terminado
                self.turn = "O" if self.turn == "X" else "X"  # Cambia el turno al otro jugador
                self.message.config(text=f"Turno de: {self.turn}")  
                if self.turn == "O":  # Si es el turno de la computadora
                    self.computer_play() 

    def computer_play(self):  # Define el método para que la computadora realice un movimiento
        x, y = self.computer_player.get_best_move()  # Obtiene el mejor movimiento posible de la computadora
        self.play(x, y)  
        
    def check_winner(self):  # Define el método para verificar si hay un ganador
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != ' ':
                self.end_game(self.buttons[i][0]['text'])  # Si hay un ganador, termina el juego y muestra el mensaje
        for i in range(3):
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != ' ':
                self.end_game(self.buttons[0][i]['text'])  
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != ' ':
            self.end_game(self.buttons[0][0]['text'])  
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != ' ':
            self.end_game(self.buttons[0][2]['text'])  
        if self.check_tie():  # Si no hay ganador y hay un empate
            self.end_game('tie')  # Termina el juego y muestra el mensaje de empate

    def check_tie(self):  # Define el método para verificar si hay un empate
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]['text'] == ' ':
                    return False  # Si hay una casilla vacía, el juego no está empatado
        return True  # Si no hay casillas vacías, el juego está empatado

    def end_game(self, winner):  # Define el método para terminar el juego y mostrar el mensaje final
        self.game_over = True  # Marca el juego como terminado
        if winner == 'tie':  # Si el juego terminó en empate
            message = "¡Empate!"  
        else:  # Si hay un ganador
            message = f"¡{winner} ganó!"  
        self.message.config(text=message)  
        play_again = messagebox.askyesno("Juega otra vez", "¿Quieres jugar de nuevo?")  
        if play_again:  # Si el jugador quiere jugar de nuevo
            self.board = [[" " for i in range(3)] for j in range(3)]  # Reinicia el tablero
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j].config(text=" ", fg="black")  # Reinicia los botones del tablero
            self.turn = "X"  
