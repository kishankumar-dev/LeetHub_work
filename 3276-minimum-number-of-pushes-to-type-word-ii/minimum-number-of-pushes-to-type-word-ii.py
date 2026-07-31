class Solution:
    def minimumPushes(self, word: str) -> int:

        freq = [0] * 26
        max_freq = 0

        # Count frequencies
        for ch in word:
            idx = ord(ch) - ord('a')
            freq[idx] += 1
            max_freq = max(max_freq, freq[idx])

        # Bucket sort frequencies
        bucket = [0] * (max_freq + 1)

        for f in freq:
            if f > 0:
                bucket[f] += 1

        ans = 0
        rank = 0  # Position among used letters

        # Process frequencies from highest to lowest
        for f in range(max_freq, 0, -1):

            while bucket[f] > 0:

                press = (rank // 8) + 1

                ans += press * f

                rank += 1
                bucket[f] -= 1

        return ans