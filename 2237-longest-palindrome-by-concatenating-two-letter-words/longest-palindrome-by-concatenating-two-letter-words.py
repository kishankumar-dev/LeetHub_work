class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt, res = Counter(words), 0
        for w, c in cnt.items():
            rev = w[::-1]
            if w < rev and rev in cnt:
                res += 4 * min(c, cnt[rev])

        for w, c in cnt.items():
            if w[0] == w[1]:    
                res += 4 * (c // 2)

        if any(w[0] == w[1] and cnt[w] % 2 for w in cnt):
            res += 2
            
        return res