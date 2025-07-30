class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        max_streak = max(
            len(list(values))
            for key, values in groupby(nums)
            if key == max_val
        )
        return max_streak