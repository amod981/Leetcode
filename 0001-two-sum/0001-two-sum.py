class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
        for i,x in enumerate(nums):
            for j,y in enumerate(nums[i+1:]):
                if x + y == target:
                    return [i,j+i+1]