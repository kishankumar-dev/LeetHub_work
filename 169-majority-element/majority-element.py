class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        rep=len(nums)/2

        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for k,v in dic.items():
            if v>rep:
                return k
        