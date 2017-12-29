import sys
from operator import mul, add, sub, truediv
from collections import deque
from pylearn.linkedlist import ListNode as ln


class Solution:

    def romanToInt(self, s):
        """
        https://leetcode.com/problems/roman-to-integer/description/
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0

        roman = {
            'I': 1,
            'II': 2,
            'III': 3,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        nums = list(map(lambda x: roman[x], list(s)))

        int_repr = []
        n = len(nums)
        should_skip = False

        for i in range(n):

            # subtractive notation
            if i < n - 1 and nums[i] < nums[i + 1]:
                int_repr.append(nums[i + 1] - nums[i])
                should_skip = True

            elif not should_skip:
                int_repr.append(nums[i])

            else:
                should_skip = not should_skip

        return sum(int_repr)

    def addTwoNumbers(self, l1, l2):
        """
        https://leetcode.com/problems/add-two-numbers/description/
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        from collections import deque
        l1_iter = l1
        l2_iter = l2
        l1_val = deque([])
        l2_val = deque([])

        while True:

            if l1_iter is None and l2_iter is None:
                break

            if l1_iter is not None:
                l1_val.appendleft(str(l1_iter.val))
                l1_iter = l1_iter.next

            if l2_iter is not None:
                l2_val.appendleft(str(l2_iter.val))
                l2_iter = l2_iter.next

        l1_val = int(''.join(l1_val))
        l2_val = int(''.join(l2_val))

        #print("{} + {} = {}".format(l1_val, l2_val, l1_val + l2_val))

        sum_val = str(l1_val +  l2_val)[::-1]
        head = None
        cur = None

        for digit in sum_val:

            if head is None:
                head = ListNode(int(digit))
                cur = head
                continue

            cur.next = ListNode(int(digit))
            cur = cur.next

        return head

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

    def findTheDifference(self, s, t):
        """
        https://leetcode.com/problems/find-the-difference/description/
        :type s: str
        :type t: str
        :rtype: str
        """
        from string import ascii_lowercase
        from operator import mul
        from functools import reduce

        if s == '' or t == '':
            return ''

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        char_prime = { k: v for k, v in zip(ascii_lowercase, primes) }
        prime_char = { k: v for k, v in zip(primes, ascii_lowercase) }

        s_num = reduce(mul, list(map(lambda x: char_prime[x], s)), 1)
        t_num = reduce(mul, list(map(lambda x: char_prime[x], t)), 1)

        if t_num > s_num:
            return prime_char[t_num / s_num]
        else:
            return prime_char[s_num / t_num]

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter
        ransom = Counter(ransomNote)
        mag = Counter(magazine)

        for letter in ransom:
            if ransom.get(letter, 0) > mag.get(letter, -1):
                return False

        return True

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        nums = []
        for i in range(left, right + 1):
            if i % 10 == 0:
                continue

            should_add = True
            num = str(i)

            for digit in num:
                if i % int(digit) != 0:
                    should_add = False

            if should_add:
                nums.append(i)

        return nums

    def reversePairsI(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pairs = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > 2 * nums[j]:
                    pairs += 1
        return pairs

    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        from sys import maxsize
        n = len(nums) - k + 1
        greatest_average = -maxsize

        for i in range(n):
            greatest_average = max(float(sum(nums[i: i + k])) / k, greatest_average)

        return greatest_average

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        from string import ascii_uppercase
        from collections import deque

        num_to_char = lambda x: ascii_uppercase[x - 1]
        num = deque([])
        ascii_len = len(ascii_uppercase)

        while True:

            if n <= ascii_len:
                num.appendleft(num_to_char(n % ascii_len))
                break

            num.appendleft(num_to_char(n % ascii_len))
            n //= ascii_len

        return ''.join(num)



    def evalRPN(self, tokens):
        """
        https://leetcode.com/problems/evaluate-reverse-polish-notation/
        :type tokens: List[str]
        :rtype
        """
        ops = {
            '*': mul,
            '+': add,
            '-': sub,
            '/': truediv
        }

        stack = deque()

        for token in tokens:
            if token in ops:
                y = int(stack.pop())
                x = int(stack.pop())
                op = ops[token]
                stack.append(op(x, y))
            else:
                stack.append(token)

        return stack.pop()

    def findPeakElement(self, nums):
        """
        https://leetcode.com/problems/find-peak-element/description/
        :type nums: List[int]
        :rtype: int
        """
        from sys import maxsize
        nums.append(-maxsize)
        nums.insert(0, -maxsize)
        n = len(nums)

        for j in range(1, n - 1):
            ni = nums[j - 1]
            nj = nums[j]
            nk = nums[j + 1]

            if ni < nj and nj > nk:
                return j - 1

        return None

    def updateMatrix(self, matrix):
        """
        https://leetcode.com/problems/01-matrix/description/
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

s = Solution()
"""
print(s.findPeakElement([1, 2, 3, 1]))
print(s.evalRPN(["2", "1", "+"]))
assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
assert s.evalRPN(["4", "13", "5", "/", "+"]) == 6
print(s.convertToTitle(1))
print(s.convertToTitle(26))
print(s.convertToTitle(28))
print(s.convertToTitle(27))
print(s.convertToTitle(56))
print(s.findMaxAverage([1,12,-5,-6,50,3], 4))
print(s.reversePairs([1,3,2,3,1]))
print(s.reversePairs([2,4,3,5,1]))
print(s.findTheDifference('abcde','bacd'))
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

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class NumArray:
    """
    https://leetcode.com/problems/range-sum-query-mutable/description/
    """
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.vals = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.vals[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.vals[i: j + 1])
