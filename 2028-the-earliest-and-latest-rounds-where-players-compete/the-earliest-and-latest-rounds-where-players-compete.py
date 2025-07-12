class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        # Solution 2:
        @lru_cache(None)
        def dp(l, r, k):
            if l == r: return (1, 1)
            if l > r:  return dp(r, l, k)
            half_k = k // 2
            half_k1 = (k + 1) // 2
            min_s = l + r - half_k
            max_s = half_k1
            a, b = inf, -inf
            for i in range(1, l + 1):
                low1 = l - i + 1
                high1 = r - i
                low2 = min_s - i
                high2 = max_s - i
                j_low = low1 if low1 > low2 else low2
                j_high = high1 if high1 < high2 else high2
                if j_low > j_high:  continue
                for j in range(j_low, j_high + 1):
                    x, y = dp(i, j, half_k1)
                    a = x + 1 if x + 1 < a else a
                    b = y + 1 if y + 1 > b else b
            return (a, b)
        return list(dp(firstPlayer, n - secondPlayer + 1, n))


        # Solution 1:
        @lru_cache(None)
        def dp(l, r, k):
            if l == r:  return (1, 1)
            if l > r:   return dp(r, l, k)
            a, b = inf, -inf
            for i in range(1, l + 1):
                for j in range(l - i + 1, r - i + 1):
                    s = i + j
                    if l + r - k // 2 <= s <= (k + 1) // 2:
                        x, y = dp(i, j, (k + 1) // 2)
                        if x + 1 < a: a = x + 1
                        if y + 1 > b: b = y + 1
            return (a, b)
        return list(dp(firstPlayer, n - secondPlayer + 1, n))