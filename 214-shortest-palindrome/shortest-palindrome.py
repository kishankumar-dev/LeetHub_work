class Solution:
    def shortestPalindrome(self, s: str) -> str:

        rev_s = s[::-1]

        new_s = s + "#" + rev_s
        
        lps = [0] * len(new_s)
        j = 0 
        
        for i in range(1, len(new_s)):
            while (j > 0 and new_s[i] != new_s[j]):
                j = lps[j - 1]
            if new_s[i] == new_s[j]:
                j += 1
                lps[i] = j
        
        longest_palindromic_prefix_len = lps[-1]
        
        return rev_s[:len(s) - longest_palindromic_prefix_len] + s