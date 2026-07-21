class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        baselineOnes = s.count('1')

        zeroBlocks = []
        currentZeroes = 0

        for char in s:
            if char == "0":
                currentZeroes += 1
            else:
                if currentZeroes > 0:
                    zeroBlocks.append(currentZeroes)
                    currentZeroes = 0
        
        if currentZeroes > 0:
              zeroBlocks.append(currentZeroes)
            
        
        maxProfit = 0
        if len(zeroBlocks) >= 2:
            for i in range(len(zeroBlocks) - 1):
                profit = zeroBlocks[i] + zeroBlocks[i + 1]
                if profit > maxProfit:
                    maxProfit = profit
        
        return baselineOnes + maxProfit