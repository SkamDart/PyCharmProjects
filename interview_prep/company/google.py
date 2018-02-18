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

from collections import deque
def licenseKeyFormatting(S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """

    s = S.replace("-", "")
    license_key = []
    ls = None

    # if first part is uneven, i.e. len(s) % k != 0
    # then append to license_key right away
    k = len(s) % K

    if k != 0:
        license_key.append(s[:k].upper())
        ls = deque(s[k:])
    else:
        ls = deque(s)

    subkey = []
    while len(ls):
        c = ls.popleft().upper()
        subkey.append(c)

        if len(subkey) == K:
            license_key.append("".join(subkey.copy()))
            subkey = []

    return "-".join(license_key)

def repeatedStringMatch(A, B):
    C = A
    append_count = 1
    while len(C) = 2 * len(A) + len(B)
        if B in C:
            return append_count
        append_count += 1
        C += A

def increment_time(self, time):
    h, m = list(map(int, time.split(":")))
    m = (m + 1) % 60
    if m == 0:
        h += 1
        m = '00'

    if m != '00' and m < 10:
        m = '0' + str(m)

    if h == 24:
        h = '00'

    if h != '00' and h < 10:
        h = '0' + str(h)

    return ':'.join(list(map(str, [h, m])))

def nextClosestTime(self, time):
    """
    :type time: str
    :rtype: str
    """
    nums = set(time)
    check = lambda x: x in nums 
    while True:
        time = self.increment_time(time)
        if all(map(check, time)):
            return time

def longestUnivaluePath(root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.len = 0

        def max_path(node):
            if not node:
                return 0

            left = max_path(node.left)
            right = max_path(node.right)
            left_path = 0
            right_path = 0
            
            if node.left and node.left.val == node.val:
                left_path += (left + 1)
            if node.right and node.right.val == node.val:
                right_path += (right + 1) 

            self.len = max(self.len, left_path + right_path)
            return max(left_path, right_path)
        
        max_path(root)
        return self.len
    
from bisect import bisect_right
def kEmptySlots(flowers, k):
    blooming = []
    for day, flower in enumerate(flowers):
        insert_idx = bisect_right(blooming, flower)
        blooming_slice = slice(insert_idx - (insert_idx > 0), insert_idx + 1)
        neighborhood = blooming[blooming_slice]
        for neighbor in neighborhood
            if abs(neighbor - flower) - 1 == k:
                return day
            blooming.insert(insert_idx, flower)
    return -1
