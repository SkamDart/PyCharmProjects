"""
Standard 2048 Game
"""

class Game(object):
    """
    Game class for a
    """
    def __init__(self, board):
        """
        """
        self.board = board

    def __str__(self):
        """
        :return:
        """
        return self.board.__str__()

    @classmethod
    def is_filled(cls, x):
        """
        End game if we have a negative element on board or
        all of the elements on the board are filled
        :param x:
        :return:
        """
        return x != 0 and x < 0

    def is_over(self):
        """
        Checks game ending conditions by checking if each square
        is filled on the board
        :return: bool whether game is over or not
        """
        return all(map(self.is_filled, self.board))
