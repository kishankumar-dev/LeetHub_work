class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        # store all gaps for convenience
        gaps = [startTime[0]]
        for i in range(1, len(startTime)):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])

        # prefs: max gap to left
        prefs = [gaps[0]]
        for i in range(1, len(gaps) - 1):
            prefs.append(max(prefs[-1], gaps[i]))
        
        # suffs: max gap to right
        suffs = [gaps[-1]]
        for i in range(len(gaps) - 2, 0, -1):
            suffs.append(max(suffs[-1], gaps[i]))
        suffs = list(reversed(suffs))

        ans, N = 0, len(startTime)

        for i, (start, end) in enumerate(zip(startTime, endTime)):
            # consider current slot
            slot = end - start
            # consider gaps immediately to left and right
            lGap, rGap = gaps[i], gaps[i + 1]
            # try and find the biggest gap before the left slot
            bestLeft = -1 if i == 0 else prefs[i - 1]
            # try and find the biggest gap after the right slot
            bestRight = -1 if i == N - 1 else suffs[i + 1]
            # we can always shift the slot within its gaps...
            time = lGap + rGap
            # ...but if there's space outside of its gaps we can move entirely 
            if bestLeft >= slot or bestRight >= slot:
                time += slot
            ans = max(ans, time)
        
        return ans