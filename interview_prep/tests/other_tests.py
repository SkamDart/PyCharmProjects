from unittest import TestCase
from pylearn.leetcode import Solution


class OtherTests(TestCase):

    def setUp(self):
        self.s = Solution()

    def test_perfect_squares(self):
        self.assertTrue(self.s.num_squares(13) == 2)
        self.assertTrue(self.s.num_squares(9) == 1)
        print(self.s.num_squares(12))
        self.assertTrue(self.s.num_squares(12) == 3)
        self.assertTrue(self.s.num_squares(24) == 3)

    def test_subarraySum(self):
        s = self.s
        self.assertTrue(s.subarraySum([1, 1, 1], 2) == 2)
        t = s.subarraySum([1,1,1,1,1], 2)
        self.assertTrue(t == 4)
        t = s.subarraySum([1, 2, 3], 3)
        print(t)
        self.assertTrue(t == 2)
        t = s.subarraySum([1, 1, 1], 1)
        print(t)
        self.assertTrue(t == 3)