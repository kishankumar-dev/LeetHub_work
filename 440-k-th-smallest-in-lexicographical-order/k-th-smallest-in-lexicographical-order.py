class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_prefix(p, n):
            count = 0
            cur = p
            next_p = p + 1
            while cur <= n:
                count += min(next_p, n + 1) - cur
                cur *= 10
                next_p *= 10
            return count
        
        current = 1
        k -= 1
        
        while k > 0:
            count = count_prefix(current, n)
            if k >= count:
                k -= count
                current += 1
            else:
                current *= 10
                k -= 1
        
        return current