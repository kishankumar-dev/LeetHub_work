class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        heap = [(w, w, 1) for w in workerTimes]
        heapq.heapify(heap)

        last_finish_time = 0
        for _ in range(mountainHeight):
            next_time, w, units_done = heapq.heappop(heap)
            last_finish_time = next_time
            heapq.heappush(heap, (next_time + w * (units_done + 1), w, units_done + 1))

        return last_finish_time