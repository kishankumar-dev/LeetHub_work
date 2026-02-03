class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        peak = -1
        valley = n

        for i in range(n - 1):
            if peak == -1 and nums[i] >= nums[i + 1]:
                peak = i
            if valley == n and nums[-1 - i] <= nums[-2 - i]:
                valley = n - 1 - i
            if peak > 0 and valley < n - 1:
                return peak < valley and self.isDecreasing(nums, peak, valley)

        return False

    
    def isDecreasing(self, nums, a, b):
        for i in range(a, b):
            if nums[i] <= nums[i + 1]:
                return False
        return True