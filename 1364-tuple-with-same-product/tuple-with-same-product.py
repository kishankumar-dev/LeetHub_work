class Solution:
    def tupleSameProduct(self, a: List[int]) -> int:
        return 4*sum((v-1)*v for v in Counter(map(prod,combinations(a,2))).values())