class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        lt = [False] * 1440
        minTime, maxTime = 1440, 0
        
        for t in timePoints:
            h, m = t.split(":")
            s = (int(h) * 60) + int(m)
            if lt[s]:
                return 0
            lt[s] = True
            minTime = min(minTime, s)
            maxTime = max(maxTime, s)
    
        op = maxTime - minTime
        if op > 720:
            op = 1440 - op
        prev = minTime
        
    
        for i in range(minTime + 1, maxTime + 1):
            if lt[i]:
                diff = i - prev
                if diff > 720:
                    diff = 1440 - diff
                op = min(op, diff)
                prev = i
        return op