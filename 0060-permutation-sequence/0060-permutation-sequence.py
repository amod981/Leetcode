class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        ind = 1
        permutation = range(1,n+1)
        
        def next_permutation(permutation):
            next_peak = 0
            for i in range(0,n-1):
                if permutation[i+1] > permutation[i]:
                    next_peak = i+1
           
            swap_index = next_peak
            
            for i in range(next_peak,n):
                if permutation[i] >  permutation[next_peak -1]:
                    swap_index = i
                else:
                    break
            permutation[next_peak -1], permutation[swap_index] = permutation[swap_index], permutation[next_peak -1]
            temp = sorted(permutation[next_peak:n])
            for i in range(next_peak,n):
                permutation[i] = temp[i-next_peak]
            
            return permutation
        
        while ind < k+1:
            if ind == k:
                return "".join(map(str,permutation))
            permutation = next_permutation(permutation)
            ind = ind + 1    