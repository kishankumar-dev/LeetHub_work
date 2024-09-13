class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
        return [arr[r] if not l else arr[l-1] ^ arr[r] for l, r in queries]