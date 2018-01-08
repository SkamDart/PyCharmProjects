from unittest import TestCase

from company.google import Solution


class TestGoogle(TestCase):

    def setUp(self):
        self.s = Solution()

    def testPlusOne(self):
        plus = self.s.plusOne
        self.assertTrue(plus([0]) == [1])
        self.assertTrue(plus([8,0,9]) == [8, 1, 0])
        self.assertTrue(plus([9]) == [1, 0])
        self.assertTrue(plus([9,9]) == [1,0,0])
        pass

    def testSpiral(self):
        mat1 = [
                 [ 1, 2, 3 ],
                 [ 4, 5, 6 ],
                 [ 7, 8, 9 ]
                ]
        soln1 = [1,2,3,6,9,8,7,4,5]
        spiral = self.s.spiralOrder

        mat2 = [[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]
                ]
        soln2 = [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
        self.assertTrue(spiral(mat1) == soln1)
        self.assertTrue(spiral(mat2) == soln2)
