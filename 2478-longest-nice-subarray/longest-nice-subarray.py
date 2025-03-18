class Solution:
    def longestNiceSubarray(self, nums):
        n, left, right, maxi, sum = len(nums), 0, 0, 0, 0
        while right < n:
            while (sum & nums[right]) != 0:
                sum -= nums[left]
                left += 1
            sum += nums[right]
            maxi = max(maxi, right - left + 1)
            right += 1
        return maxi