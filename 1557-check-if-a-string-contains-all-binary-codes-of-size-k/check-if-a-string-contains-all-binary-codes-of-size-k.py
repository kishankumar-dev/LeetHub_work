class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        d ={}
        if len(s) < k:
            return False
        
        for i in range(0, len(s) - k +1):
            cur = s[i:i+k]
            if cur not in d.keys():
                d[cur] = 1
                
        if len(d.keys()) == 2**k:
            return True
        else:
            return False