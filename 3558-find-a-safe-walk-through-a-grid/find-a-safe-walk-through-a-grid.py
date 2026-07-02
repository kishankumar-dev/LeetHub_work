class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        distance = [[float("inf") for _ in range(n)] for _ in range(m)]
        distance[0][0] = -health + grid[0][0]
        pq = [(distance[0][0], 0, 0)]
        while pq:
            d, i, j = heapq.heappop(pq)
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ci, cj = i + di, j + dj
                if ci < 0 or ci == m or cj < 0 or cj == n: continue
                if d + grid[ci][cj] < distance[ci][cj]:
                    distance[ci][cj] = d + grid[ci][cj]
                    heapq.heappush(pq, (d + grid[ci][cj], ci, cj))
        return distance[m - 1][n - 1] < 0