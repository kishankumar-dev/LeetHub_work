class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        y = sum(chalk)
        x = k//y
        k -= (x*y)
        for x in range(len(chalk)):
            if chalk[x]>k:
                return x
            else:
                k -= chalk[x]