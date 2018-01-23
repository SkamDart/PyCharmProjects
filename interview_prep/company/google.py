"""
"""

class Solution:

    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        C = ''
        reps = 0
        while len(C) < 2 * len(A) + len(B):
          if B in C:
            return reps
          reps += 1
          C += A
        return -1
        
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        pass

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        while True:

            for node in lists:
                pass

    def trap(self, height):
        """
        https://leetcode.com/explore/interview/card/google/array-and-strings/341/
        :type height: List[int]
        :rtype: int
        """
        pass

    def spiralOrderI(self, matrix):
        if matrix == []:
            return []

        spiral = []

        while matrix:
            # raindrop, pop TOP
            spiral.append(matrix.pop(0))

            if matrix and matrix[0]:
                # RIGHT
                for row in matrix:
                    spiral.append(row.pop())

            if matrix:
                # BOTTOM
                spiral.append(matrix.pop()[::-1])

            if matrix and matrix[0]:
                # LEFT
                for row in reversed(matrix):
                    spiral.append(row.pop(0))

        return spiral

    def spiralOrder(self, matrix):
        """
        https://leetcode.com/explore/interview/card/google/array-and-strings/338/
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []

        from collections import deque
        spiral = deque([])

        while matrix:

            # pops first "element" whether it is row or element
            first_row = matrix.pop(0)
            for elem in first_row:
                spiral.append(elem)

            if matrix and matrix[0]:
                for row in matrix:
                    # removes "element" at end of each row
                    spiral.append(row.pop())

            if matrix:
                # remove bottom row but append in reverse order
                last_row = matrix.pop()[::-1]
                for col in last_row:
                    spiral.append(col)

            if matrix and matrix[0]:
                for row in reversed(matrix):
                    # removes element at beginning of each row
                    spiral.append(row.pop(0))

        return list(spiral)

    def plusOne(self, digits):
        """
        https://leetcode.com/explore/interview/card/google/array-and-strings/339/
        :type digits: List[int]
        :rtype: List[int]
        """
        from collections import deque
        new_sum = deque([])
        digits[-1] += 1
        carry_over = 0

        for digit in reversed(digits):
            digit += carry_over
            new_sum.appendleft(digit % 10)

            if digit >= 10:
                carry_over = 1
            else:
                carry_over = 0

        if carry_over == 1:
            new_sum.appendleft(1)

        return list(new_sum)

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        pass

    def licenseKeyFormattingII(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace('-', '')
        len_S = len(S)

        keys = []

        if len_S % K != 0:
            first = slice(0, len_S % K)
            k = len_S % K
        else:
            first = slice(0, K)
            k = K

        keys.append(S[first])

        for i in range(1, n_iter + 1):
            mid = slice(i * K - k, (i + 1) * K - k)
            keys.append(''.join(S[mid]))
            #print("{}: {}".format(i, keys[i]))

        return '-'.join(keys)

    def licenseKeyFormatting(self, S, K):
        keys = []
        S = S.upper().replace("-", "")
        step_size = K
        n_steps = len(S) // K

        for i in range(0, n_steps):
            slice_dad = slice(i * step_size, (i + 1) * step_size)
            keys.append(S[slice_dad])
            # print("slice: {}".format(slice_dad))
            # print("{}".format(S[slice_dad]))

        return '-'.join(keys)

from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        self._capacity = size
        self._data = deque([])
        self._total = 0
        self._size = 0

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, new_capacity):
        self._capacity = new_capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        self._size = new_size

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, new_total):
        self._total = new_total

    def next(self, val):
        if self.size == self.capacity:
            # evict oldest value
            evicted_value = self._data.pop()
            # subtract that value from total
            self.total -= evicted_value
        else:
            # increase size
            self.size += 1

        self.total += val
        self._data.appendleft(val)
        return self.total / self.size

if __name__ == '__main__':
    s = Solution()
    m = MovingAverage(3)
