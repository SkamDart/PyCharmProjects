

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

if __name__ == '__main__':
    s = Solution()
    empty = []
    empty_soln = 0
    basic = [1, 2, 3]
    basic_soln = 4

    assert s.rob(empty) == empty_soln
    assert s.rob(basic) == basic_soln
    assert s.rob([1, 5, 10, 75, 100, 5]) == 111
