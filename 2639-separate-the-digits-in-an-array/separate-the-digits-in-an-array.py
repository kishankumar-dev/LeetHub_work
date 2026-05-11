class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for num in nums:
            for dig in str(num):
                ans.append(int(dig))
        return ans