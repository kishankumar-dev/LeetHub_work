class Solution:
    def even(self, num):
        return num // 2
    def odd(self, num):
        return num - 1
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num = self.even(num)
            else:
                num = self.odd(num)
            steps += 1
        return steps