from random import randint

class ComputerPlayer:
    def __init__(self, game):
        self.game = game

    def get_best_move(self):
        for player in ('O', 'X'):
            for i in range(3):
                if self.game.buttons[i][0]['text'] == self.game.buttons[i][1]['text'] == player and self.game.buttons[i][2]['text'] == ' ':
                    return i, 2
                if self.game.buttons[i][0]['text'] == self.game.buttons[i][2]['text'] == player and self.game.buttons[i][1]['text'] == ' ':
                    return i, 1
                if self.game.buttons[i][1]['text'] == self.game.buttons[i][2]['text'] == player and self.game.buttons[i][0]['text'] == ' ':
                    return i, 0
                if self.game.buttons[0][i]['text'] == self.game.buttons[1][i]['text'] == player and self.game.buttons[2][i]['text'] == ' ':
                    return 2, i
                if self.game.buttons[0][i]['text'] == self.game.buttons[2][i]['text'] == player and self.game.buttons[1][i]['text'] == ' ':
                    return 1, i
                if self.game.buttons[1][i]['text'] == self.game.buttons[2][i]['text'] == player and self.game.buttons[0][i]['text'] == ' ':
                    return 0, i
                if self.game.buttons[0][0]['text'] == self.game.buttons[1][1]['text'] == player and self.game.buttons[2][2]['text'] == ' ':
                    return 2, 2
                if self.game.buttons[0][2]['text'] == self.game.buttons[1][1]['text'] == player and self.game.buttons[2][0]['text'] == ' ':
                    return 2, 0
                if self.game.buttons[1][1]['text'] == self.game.buttons[2][2]['text'] == player and self.game.buttons[0][0]['text'] == ' ':
                    return 0, 0
                if self.game.buttons[2][0]['text'] == self.game.buttons[1][1]['text'] == player and self.game.buttons[0][2]['text'] == ' ':
                    return 0, 2
        for player in ('O', 'X'):
            opponent = 'O' if player == 'X' else 'X'
            for i in range(3):
                if self.game.buttons[i][0]['text'] == self.game.buttons[i][1]['text'] == opponent and self.game.buttons[i][2]['text'] == ' ':
                    return i, 2
                if self.game.buttons[i][0]['text'] == self.game.buttons[i][2]['text'] == opponent and self.game.buttons[i][1]['text'] == ' ':
                    return i, 1
                if self.game.buttons[i][1]['text'] == self.game.buttons[i][2]['text'] == opponent and self.game.buttons[i][0]['text'] == ' ':
                    return i, 0
        if self.game.buttons[1][1]['text'] == ' ':
            return 1, 1
        for i in range(3):
            for j in range(3):
                if self.game.buttons[i][j]['text'] == ' ':
                    return i, j
        return randint(0, 2), randint(0, 2)