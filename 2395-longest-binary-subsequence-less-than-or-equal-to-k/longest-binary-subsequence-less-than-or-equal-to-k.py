class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        S = [int(i) for i in s]
        zero = S.count(0)

        S = S[::-1]
        n = len(S)

        sm = 0
        count = 0
        for i in range(n):
            v = 2 ** i  # Correct: LSB (i = 0) is 1, not 0
            if S[i] == 1:
                if sm + v <= k:
                    sm += v
                    count += 1
                else:
                    continue  # Skip this '1', not break
            else:
                count += 1
                zero -= 1  # Track how many '0's we've used

        return count + zero  # Add back remaining free '0's