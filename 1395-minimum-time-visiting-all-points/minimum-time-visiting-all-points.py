class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs(P[0]-Q[0]), abs(P[1]-Q[1])) for P, Q in pairwise(points))