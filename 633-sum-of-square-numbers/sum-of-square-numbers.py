class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(0, int(c**0.5) + 1):
            j_squared = c - i * i
            j = int(j_squared**0.5)
            if j * j == j_squared:
                return True
        return False