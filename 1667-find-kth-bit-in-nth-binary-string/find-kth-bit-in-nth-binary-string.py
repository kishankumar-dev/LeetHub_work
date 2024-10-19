class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        noda = [1]
        for i in range(1, n):
            noda.append(2 * noda[i - 1] + 1)

        def findDigit(i, n):
            if n == 0:
                return '0'
            mid = (noda[n] - 1) // 2
            if i == mid:
                return '1'
            elif i < mid:
                return findDigit(i, n - 1)
            else:
                return '1' if findDigit(mid - (i - mid), n - 1) == '0' else '0'

        return findDigit(k - 1, n - 1)
        