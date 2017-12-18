import sys


class Solution:

    def spiral_order(self, matrix):
        """
        :param matrix:
        :return:
        """
        if not matrix:
            return []

        spiral = []

        while matrix:

            spiral += matrix.pop(0)

            if matrix and matrix[0]:
                for row in matrix:
                    spiral.append(row.pop())

            if matrix:
                spiral += matrix.pop()[::-1]

            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    spiral.append(row.pop(0))

        return spiral

    def generate_matrix(self, n):
        """
        :param n:
        :return:
        """
        pass

    def find_second_min_val(self, root, mins):
        if root is None:
            return mins[1]

    def find_second_minimum_value(self, root):
        return self.find_second_min_val(root, (sys.maxsize, sys.maxsize))


    def is_perfect_square(self, n):
        """

        :param n:
        :return:
        """
        sqrt = n ** .5
        return sqrt ** 2 == n

    def is_prime(self, n):
        for i in range(3, n):
            if n % i == 0:
                return False

        if n != 1:
            return True
        else:
            return False

    def num_squares(self, n):
        """

        :param n:
        :return:
        """
        from math import sqrt

        sqrt_n = sqrt(n)
        is_perfect_square = sqrt_n ** 2 == n

        if is_perfect_square:
            """
            Obvious
            It's sum is itself if it's a perfect square
            """
            return 1

        elif self.is_prime(n):
            """
            Not so obvious
            Fermat's Theorem
            All primes are the sum of two perfect squares
            p = x ** 2 + y ** 2
            """
            return 2

        else:
            """
            Legendre's 4 Prime Theorem
            """
            num_squares = int(sqrt_n) + 1
            perfect_squares = [i ** 2 for i in range(1, num_squares)]
            N = n + 1

            factors = self.factorize(n)

            print('factors ', factors)

            length = len(perfect_squares)

            for i, factor in enumerate(reversed(factors)):
                print('factor ', factor)
                if factor in perfect_squares:
                    return factors[length - i + 1]

            # not sure if it will hit here or not
            return -1

    def factorize(self, n):
        N = n + 1

        factors = []

        for i in range(1, N):
            if n % i == 0:
                factors.append(i)

        return factors

    def subarraySum(self, nums, k):
        n = len(nums)
        k_sum_count = 0

        for i in range(n):
            if nums[i] == k:
                k_sum_count += 1
            for j in range(i + 1, n):
                if sum(nums[i:(j+1)]) == k:
                    k_sum_count += 1

        return k_sum_count

    def findRestaurant(self, list1, list2):
        #l1 = { v: k for k, v in enumerate(list1) }
        l2 = { v: k for k, v in enumerate(list2) }
        min_indices = [(1000000, 1000000)]

        for l1_idx, li in enumerate(list1):
            if li in l2:
                l2_idx = l2[li]
                idx_sum = l1_idx + l2_idx
                min_sum = sum(min_indices[0])

                if idx_sum <  min_sum:
                    min_indices = [(l1_idx, l2_idx)]
                elif idx_sum == min_sum:
                    min_indices.append((l1_idx, l2_idx))
                else:
                    continue

        return [list1[tuple[0]] for tuple in min_indices]

    def levelOrder(self, root):
        if not root:
            return [[]]

        level_begin = 0
        level_end = 1
        tree = []

        while True:

            if level_begin > len(root):
                break

            level_slice = slice(level_begin, level_end)
            level = [ x for x in root[level_slice] if isinstance(x, int)]
            tree.append(level)
            level_begin = level_end
            level_end = 2 ** (level_begin + 1) - 1

        return tree

    def height(self, root):

        if root is None:
            return 1

        return 1 + max(self.height(root.left), self.height(root.right))

    def levelOrder(self, root):
        from collections import deque
        if not root:
            return [[]]

        queue = deque([root])
        seen = { root }

    @staticmethod
    def str_math(a, b, op):
        if op == '-':
            return a - b
        elif op == '+':
            return a + b
        elif op == '*':
            return a * b
        else:
            return None

    @staticmethod
    def is_op(exp):
        return exp in "+-*"

    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]

        ways = []
        for i, ci in enumerate(input):
            if Solution.is_op(ci):
                start = self.diffWaysToCompute(input[:i])
                end  = self.diffWaysToCompute(input[i+1:])
                for j in start :
                    for k in end:
                        ways.append(Solution.str_math(j, k, ci))
        return ways

    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

s = Solution()

"""
print(s.diffWaysToCompute("2-1"))
print(s.diffWaysToCompute("2-1-1"))
print(s.levelOrder([3,9,20,None,None,15,7]))
l1 = ["Shogun","Tapioca Express","Burger King","KFC"]
l2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
k1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
k2 = ["KFC", "Shogun", "Burger King"]
print(s.findRestaurant(l1, l2))
print(s.findRestaurant(k1, k2))
"""

