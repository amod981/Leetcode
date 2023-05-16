class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        def binary_search_for_pivot(array,l,r):
            
            mid = l + (r -l)/2
            print(l,r,mid)
            if (array[l] < array[r]):
                return l
            elif l == r:
                return l
    
            elif array[l] < array[mid]:
                return binary_search_for_pivot(array,mid,r)

            elif array[r] > array[mid]:
                return binary_search_for_pivot(array,l,mid)

            else:
                return binary_search_for_pivot(array, l+1, r)

            
        pivot_index =  binary_search_for_pivot(nums,0, len(nums) -1)
        print(pivot_index)
        if pivot_index is None:
            return nums[0]
        else:
            return nums[pivot_index]