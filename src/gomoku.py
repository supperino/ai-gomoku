import numpy as np
from enum import Enum
import utils
import ia


class Piece(Enum):
    EMPTY = '.'
    PLAYER = 'X'
    IA = 'G'


class Board:
    def __init__(self):
        self._pieces = np.full((utils.BOARD_SIZE, utils.BOARD_SIZE),
                               Piece.EMPTY.value) 
    
    def mark_piece(self, player, position):
        print(player)
        print(player.value)
        if self._pieces[position] == Piece.EMPTY.value:
            self._pieces[position] == player.value
            return True
        else:
            return False

    def __str__(self):
        return self.board_render()

    def board_render(self):
        _string_board = ''
        for index, row in enumerate(self._pieces):
            _string_board = _string_board + '  '.join(row) + '\n'
        return _string_board


class Gomoku:
    def __init__(self):
        self.board = Board()
        self.winner = None
        self.IA = ia.IA()
        self._actual_player = Piece.PLAYER

    def run_game(self):
        while not self.winner:
            utils.clear_screen()
            print(self.board)
            if not self.board.mark_piece(self._actual_player,
                                         self.player_move()):
                print('Position already used!')
                continue
            self.check_win()
            self.toggle_player()

    def check_win(self):
        pass

    def player_move(self):
        try:
            return tuple(map(int, input('X, Y > ').split(',')))
        except ValueError:
            print('Input was not a number [0..14] ')

    def toggle_player(self):
        self._actual_player = Piece.PLAYER if self._actual_player else Piece.IA


if __name__ == '__main__':
    Gomoku().run_game()
