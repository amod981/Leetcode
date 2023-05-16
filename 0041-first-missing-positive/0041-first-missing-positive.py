class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s = set(nums)
        i = 1
        while True:
            if i not in s:
                return i
            i = i + 1