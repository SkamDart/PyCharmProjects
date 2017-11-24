import numpy as np
import graphvis as gv



class Graphic():

    NOT_ITERABLE = 'PARAMETER IS NOT AN ITERABLE'

    def __init__(self, seq=[]):
        """
        Constructor for a graphic object
        :param seq:
        """
        self.seq = np.array(seq)

    def __str__(self):
        """
        Generates string representation of our graph
        Currently just prints NP array
        @TODO ASCII?
        :return:
        """
        return self.seq.tostring()



    @staticmethod
    def generate_graph(cls, seq):
        """
        Generate a
        :param cls:
        :param seq:
        :return:
        """
        if not cls.is_graphic(seq):
            raise ValueError(cls.NOT_ITERABLE)

    @staticmethod
    def is_graphic(cls, seq):
        """
        @staticmethod just means it is a class
        :param seq:
        :return:
        """
        if type(seq) is list or type(seq) is tuple or isinstance(seq, np.ndarray):
            return cls.havel_hakimi(seq)
        else:
            return False

    @staticmethod
    def havel_hakimi(cls, seq):
        """
        Given a valid sequence type, is it graph?
        :param cls:
        :param seq:
        :return:
        """