class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        coverage = [0] * n
        curr = 0
        
        for l, r in queries:
            diff[l] += 1
            if r + 1 < len(diff):
                diff[r + 1] -= 1
        
        for i in range(n):
            curr += diff[i]
            coverage[i] = curr
        
        for i in range(n):
            if coverage[i] < nums[i]:
                return False
            
        return True        