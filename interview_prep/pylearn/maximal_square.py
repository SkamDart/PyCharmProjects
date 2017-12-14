class Solution:
    def print_list(self, l):
        for i, row in enumerate(l):
            print("{}".format(row))

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_square_area = 0

        for i, row in enumerate(matrix):
            for j, entry in enumerate(row):
                matrix[i][j] = int(matrix[i][j])
                if i and j and matrix[i][j]:
                    matrix[i][j] = min(matrix[i][j - 1],
                                       matrix[i - 1][j],
                                       matrix[i - 1][j - 1]) + 1
                max_square_area = max(max_square_area, matrix[i][j] ** 2)

        return max_square_area


if __name__ == '__main__':
    s = Solution()
    print(s.maximalSquare([["1","0","1","0","0"],
                           ["1","0","1","1","1"],
                           ["1","1","1","1","1"],
                           ["1","0","0","1","0"]])
                           )
    print(s.maximalSquare([["1"]]))
    print(s.maximalSquare([["0"]]))

