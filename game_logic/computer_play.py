from random import randint

class ComputerPlayer:
    def __init__(self, game):
        self.game = game

    def get_best_move(self):
        # Verificar si hay una jugada ganadora o de bloqueo para el jugador actual y la computadora
        for jugador in ('O', 'X'):
            for i in range(3):
                # Verifica filas para ganar o bloquear
                if self.juego.botones[i][0]['text'] == self.juego.botones[i][1]['text'] == jugador and self.juego.botones[i][2]['text'] == ' ':
                    return i, 2
                if self.juego.botones[i][0]['text'] == self.juego.botones[i][2]['text'] == jugador and self.juego.botones[i][1]['text'] == ' ':
                    return i, 1
                if self.juego.botones[i][1]['text'] == self.juego.botones[i][2]['text'] == jugador and self.juego.botones[i][0]['text'] == ' ':
                    return i, 0
                # Verifica columnas para ganar o bloquear
                if self.juego.botones[0][i]['text'] == self.juego.botones[1][i]['text'] == jugador and self.juego.botones[2][i]['text'] == ' ':
                    return 2, i
                if self.juego.botones[0][i]['text'] == self.juego.botones[2][i]['text'] == jugador and self.juego.botones[1][i]['text'] == ' ':
                    return 1, i
                if self.juego.botones[1][i]['text'] == self.juego.botones[2][i]['text'] == jugador and self.juego.botones[0][i]['text'] == ' ':
                    return 0, i
                # Verifica diagonales para ganar o bloquear
                if self.juego.botones[0][0]['text'] == self.juego.botones[1][1]['text'] == jugador and self.juego.botones[2][2]['text'] == ' ':
                    return 2, 2
                if self.juego.botones[0][2]['text'] == self.juego.botones[1][1]['text'] == jugador and self.juego.botones[2][0]['text'] == ' ':
                    return 2, 0
                if self.juego.botones[1][1]['text'] == self.juego.botones[2][2]['text'] == jugador and self.juego.botones[0][0]['text'] == ' ':
                    return 0, 0
                if self.juego.botones[2][0]['text'] == self.juego.botones[1][1]['text'] == jugador and self.juego.botones[0][2]['text'] == ' ':
                    return 0, 2
        # Verifica si el centro está vacío
        if self.juego.botones[1][1]['text'] == ' ':
            return 1, 1
        # Si no hay jugadas ganadoras, de bloqueo o centro vacío, elige una casilla aleatoria
        for i in range(3):
            for j in range(3):
                if self.juego.botones[i][j]['text'] == ' ':
                    return i, j
        # Si todas las casillas están ocupadas, elige una casilla aleatoria
        return randint(0, 2), randint(0, 2)
