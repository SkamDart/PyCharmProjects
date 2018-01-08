

class Solution:

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


if __name__ == '__main__':
    s = Solution()
    print(s.licenseKeyFormatting("5F3Z-2e-9-w", 4))
    print(s.licenseKeyFormatting("2-5g-3-J", 2))