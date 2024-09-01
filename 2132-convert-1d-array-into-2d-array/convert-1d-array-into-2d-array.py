class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = []
        temp = []
        if len(original) != m*n:
            return []
        for i in range (len(original)):
            temp.append(original[i])
            if (i+1) % n == 0:
                result.append(temp)
                temp = []
        return result

