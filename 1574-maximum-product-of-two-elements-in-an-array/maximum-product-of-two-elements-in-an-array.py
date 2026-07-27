class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        d1 = d2 = 0
        for a in nums:
            if d1 <= a:
                d2 = d1
                d1 = a
            elif d2 < a:
                d2 = a
        return (d1 - 1) * (d2 - 1)