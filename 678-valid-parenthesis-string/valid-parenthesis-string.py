class Solution:
    def checkValidString(self, s: str) -> bool:
        N = len(s)

        @cache

        def f(index, acc):
            if index == N:
                return not acc
            if s[index] == '(':
                if f(index+1, acc+1):
                    return True
            elif s[index] == ')':
                if acc and f(index+1, acc-1):
                    return True
            else:
                if f(index+1, acc) or f(index+1, acc+1) or (acc and f(index+1, acc-1)):
                    return True
            return False   
        return f(0, 0)