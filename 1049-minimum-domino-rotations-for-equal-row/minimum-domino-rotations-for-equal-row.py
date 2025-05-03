class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x, A, B):
            rotations = 0
            for a, b in zip(A, B):
                if a == x:
                    continue
                if b == x:
                    rotations += 1
                else:
                    return float('inf')
            return rotations

        candidates = {tops[0], bottoms[0]}
        n = len(tops)
        min_rotations = float('inf')
        for x in candidates:
            min_rotations = min(min_rotations, check(x, tops, bottoms), check(x, bottoms, tops))
        return min_rotations if min_rotations != float('inf') else -1