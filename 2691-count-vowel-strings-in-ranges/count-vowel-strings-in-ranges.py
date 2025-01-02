class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def is_vowel_string(word):
            vowels = "aeiouAEIOU"
            if len(word) == 1:
                return word in vowels
            return word[0] in vowels and word[-1] in vowels

       
        vowel_flags = [1 if is_vowel_string(word) else 0 for word in words]

       
        prefix_sums = [0] * (len(vowel_flags) + 1)
        for i in range(len(vowel_flags)):
            prefix_sums[i + 1] = prefix_sums[i] + vowel_flags[i]

     
        result = []
        for start, end in queries:
            result.append(prefix_sums[end + 1] - prefix_sums[start])

        return result