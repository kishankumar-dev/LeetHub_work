class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        rep=len(nums)/3
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        ar=[]
        for k,v in dic.items():
            if v>rep:
                ar.append(k)
        return ar