from functools import reduce
import numpy as np

class Solution:

    def rob(self, nums):
        """

        :param nums:
        :return:
        """
        if not nums:
            return 0

        include_loot = 0
        exclude_loot = 0

        for num in nums:

            if exclude_loot > include_loot:
                new_include = exclude_loot
            else:
                new_include = include_loot

            include_loot = exclude_loot + num
            exclude_loot = new_include

        return max(include_loot, exclude_loot)

    def maxSubArray(self, nums):
        pass

    def deleteAndEarnI(self, nums):
        if nums == []:
            return 0

        num = nums[0]
        filtered = list(filter(lambda x: x != num + 1 and num - 1 != x, nums[1:]))
        return max(num + self.deleteAndEarn(filtered), self.deleteAndEarn(nums[1:]))

    def deleteAndEarn(self, nums):
        from collections import Counter
        freq = Counter(nums)
        prev = 0
        cur = 0

        return cur

    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from sys import maxsize
        cur_min = maxsize
        cur_mid = maxsize

        # iterate through each number
        for num in nums:
            # num <= cur_min <= cur_mid
            if num <= cur_min:
                cur_min = num
            # cur_min < num <= cur_mind
            elif  num <= cur_mid:
                cur_mid = num
            else:
            # cur_min < cur_mid < num
                return True

        return False

    def manhattan(self, start, end):
        return (start[0] - end[0]) + (start[1] - end[1])

    def findPaths(self, m, n, N, i, j):
        """
        :param m:
        :param n:
        :param N:
        :param i:
        :param j:
        :return:
        """
        from collections import deque
        exits = np.zeros((m, n))
        exits[:, 0] += 1
        exits[:, -1] += 1
        exits[0, :] += 1
        exits[-1, :] += 1
        modulus = np.power(10, 9) + 7
        total_paths = 0
        queue = deque([(i, j)])

        for _ in range(0, N):
            while queue:
                node = queue.popleft()
                total_paths += exits[node]


        return np.mod(total_paths, modulus)

    def validNeighbors(self, pt, dims):
        x = pt[0]
        y = pt[1]
        m = dims[0]
        n = dims[1]

    def minCostHelp(self, cost, i):
        return min(cost[i] + self.minCostHelp(cost[i + 1:], i + 1),
                   cost[i + 1] + self.minCostHelp(cost[i + 2:], i + 2))

    def minCostClimbingStairsI(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        memoized = [0] * n
        memoized[0] = cost[0]
        memoized[1] = cost[1]

        for i in range(2, len(memoized)):
            memoized[i] = cost[i] + min(memoized[i - 2], memoized[i - 1])

        return min(memoized[-2], memoized[-1])

    def minCostClimbingStairs(self, cost):
        f1 = 0
        f2 = 0

        for ci in reversed(cost):
            f1, f2 = ci + min(f1, f2), f1

        return min(f1, f2)

    def countSubstrings(self, s):
        n = len(s)
        substring_count = 0
        s_rev = s[::-1]

        for i in range(n):
            for j in range(i, n):
                if s_rev[i:j] == s[i:j]:
                    substring_count += 1

        return substring_count

    def maxSubArray(self, nums, i):
        if i >= len(nums):
            return 0

        return max(nums[i] + self.maxSubArray(nums, i + 1),
                   self.maxSubArray(nums, i + 1))





#if __name__ == '__main__':
#    s = Solution()
    """
    empty = []
    empty_soln = 0
    basic = [1, 2, 3]
    basic_soln = 4
    assert s.rob(empty) == empty_soln
    assert s.rob(basic) == basic_soln
    assert s.rob([1, 5, 10, 75, 100, 5]) == 111
    print(s.deleteAndEarn([3, 4, 2]))
    print(s.deleteAndEarn([2, 2, 3, 3, 3, 4]))
    print(s.add(1, 2, 3))
    from operator import add, mod
    print(s.op(add, 1, 2, 3, 4, 5, 6))
    print(s.op(mod, 5, 1234))
    cost = [10, 15, 20]
    print(s.minCostClimbingStairs(cost))
    """
    #print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4], 0))

nums = [-2,1,-3,4,-1,2,1,-5,4]

max_ = 0
max_here = 0

for num in nums:
    max_here = num + max_here
    max_here = max(max_here, num)
    max_ = max(max_here, max_)

print(max_)
