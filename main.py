import tkinter as tk
from game_logic.tic_tac_toe import TicTacToe

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Juego de Totito") 
    game = TicTacToe(root)
    root.mainloop()