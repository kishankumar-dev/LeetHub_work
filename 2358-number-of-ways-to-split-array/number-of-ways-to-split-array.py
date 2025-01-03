class Solution:
    def waysToSplitArray(self, nums):
        left_sum = 0
        right_sum = sum(nums)
        ans = 0
        n = len(nums)
        
        for i in range(n - 1):
            left_sum += nums[i]
            right_sum -= nums[i]
            if left_sum >= right_sum:
                ans += 1
                
        return ans