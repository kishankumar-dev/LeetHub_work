class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        prev = word[0]
        count = 1

        for i in range(1, len(word)):
            if prev != word[i]:
                ans += str(count) + prev
                count = 1
                prev = word[i]
            else:
                if count == 9:
                    ans += str(count) + prev
                    count = 1
                else:
                    count += 1

        ans += str(count) + prev
        return ans