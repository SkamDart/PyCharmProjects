from functools import reduce


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

    def add(self, *args):
        return sum(args)

    def op(self, op, *args):
        return reduce(op, args)

if __name__ == '__main__':
    s = Solution()
    """
    empty = []
    empty_soln = 0
    basic = [1, 2, 3]
    basic_soln = 4
    assert s.rob(empty) == empty_soln
    assert s.rob(basic) == basic_soln
    assert s.rob([1, 5, 10, 75, 100, 5]) == 111
    """
    print(s.deleteAndEarn([3, 4, 2]))
    print(s.deleteAndEarn([2, 2, 3, 3, 3, 4]))
    print(s.add(1, 2, 3))
    from operator import add, mod
    print(s.op(add, 1, 2, 3, 4, 5, 6))
    print(s.op(mod, 5, 1234))
