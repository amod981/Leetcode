import heapq
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        window = []
        heapq.heapify(window)
        total = 0
        output = []
        for index,value in enumerate(nums):
            if total < k:
                total = total + 1
                heapq.heappush(window,(-1*value,index))
            else:    
                # print(index, window[0])
                while window[0][1] <  (index - k):
                    heapq.heappop(window)

                output.append(-1*window[0][0])
                heapq.heappush(window,(-1*value,index))
        
        index = index + 1
        while window[0][1] <  (index - k):
            heapq.heappop(window)

        output.append(-1*window[0][0])
        
        return output