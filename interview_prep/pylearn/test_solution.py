from unittest import TestCase
import pylearn.leetcode as solution
import pylearn.lru_cache as lru

s = solution.Solution()


class TestSolution(TestCase):

    def test_spiral(self):
        a = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ]
        b = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            ]
        c = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10]
            ]
        d = []

        assert s.spiral_order(a) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
        assert s.spiral_order(b) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        assert s.spiral_order(c) == [1, 2, 4, 6, 8, 10, 9, 7, 5, 3]
        assert s.spiral_order(d) == []

    def test_generate_matrix(self):
        pass

