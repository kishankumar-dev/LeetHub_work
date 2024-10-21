class Solution:
    def maxUniqueSplit(self, s: str) -> int:
    
        result = 0 
        memo = set() 
        def backtrack(i,curr):
            nonlocal result
            if i == len(s):
                if curr and (curr not in memo):
                    result = max(len(memo)+1,result)
                return
                     
            curr += s[i]
            if curr not in memo:
                memo.add(curr)
                backtrack(i+1,"")
                memo.remove(curr)

            backtrack(i+1,curr)

        backtrack(0,"")
        return result
        