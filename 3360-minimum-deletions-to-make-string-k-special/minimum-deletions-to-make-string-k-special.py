from collections import Counter
import bisect

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = sorted(Counter(word).values())
        n = len(freq)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + freq[i]

        total = prefix[-1]
        min_del = float('inf')
        for i in range(n):
            target = freq[i]
            max_allowed = target + k
            j = bisect.bisect_right(freq, max_allowed)
            delete_below = prefix[i]
            delete_above = total - prefix[j] - (max_allowed * (n - j))
            deletions = delete_below + delete_above

            min_del = min(min_del, deletions)

        return min_del