class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set("aeiou")
        n = len(word)
        result = 0
        next_consonant = [n] * n
        next_cons_index = n
        for i in range(n - 1, -1, -1):
            next_consonant[i] = next_cons_index
            if word[i] not in vowels:
                next_cons_index = i

        vowel_count = {}
        cons_count = 0
        left = 0 

        for right in range(n):
            ch = word[right]
            if ch in vowels:
                vowel_count[ch] = vowel_count.get(ch, 0) + 1
            else:
                cons_count += 1

            while cons_count > k and left <= right:
                left_ch = word[left]
                if left_ch in vowels:
                    vowel_count[left_ch] -= 1
                    if vowel_count[left_ch] == 0:
                        del vowel_count[left_ch]
                else:
                    cons_count -= 1
                left += 1
 
            while left <= right and cons_count == k and len(vowel_count) == 5:

                result += next_consonant[right] - right

                left_ch = word[left]
                if left_ch in vowels:
                    vowel_count[left_ch] -= 1
                    if vowel_count[left_ch] == 0:
                        del vowel_count[left_ch]
                else:
                    cons_count -= 1
                left += 1

        return result