class Solution:
    def getSneakyNumbers(self, a: List[int]) -> List[int]:
        g = lambda:chain(a,range(len(a)-2))
        q = (q:=reduce(xor,g()))&-q
        return [reduce(xor,(v for v in g() if f(v&q))) for f in (bool,not_)]