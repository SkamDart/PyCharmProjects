import numpy as np
from .Move import *


class Board(object):
    """
    Logic for the game board
    Grid is a numpy array
    """

    def __init__(self, shape=(4,4)):
        """
        :param shape: size of grid to play on
        :param n: power of two to get up to
        """
        self.grid = np.zeros(shape)

    def __str__(self):
        """
        :param self:
        :return:
        """
        return np.array_str(self.grid)


    def shift(self, move):
        """
        :param move:
        :return:
        """
        if move == Move.LEFT:
            self.shiftLeft()
        elif move == Move.RIGHT:
            self.shiftRight()
        elif move == Move.UP:
            self.moveUp()
        elif move == Move.DOWN:
            self.moveDown()
        else:
            raise ValueError('Invalid Shift of {}'.format(move))

    def injectSquare(self):
        """
        Randomly injects one square into an open spot on the board
        :return:
        """

    def shiftLeft(self):
        """
        Moves all game squares over
        :return:
        """
        pass

    def shiftRight(self):
        """
        Moves all game squares up
        :return:
        """
        pass

    def moveUp(self):
        """
        Moves all game squares up
        :return:
        """
        pass

    def moveDown(self):
        """
        Moves all games squares down
        :return:
        """
        pass