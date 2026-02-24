class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]=dic[i]+1
        l=[]
        for k,v in dic.items():
            if v>1:
                l.append(k)
        return l[0]
        