import heapq
import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = [-num for num in nums]
        heapq.heapify(pq)  # Create a max-heap (by inverting the values)
        
        score = 0
        while k > 0:
            ele = -heapq.heappop(pq)  # Get the max element (by negating)
            score += ele
            heapq.heappush(pq, -math.ceil(ele / 3))  # Insert ceil(ele / 3)
            k -= 1
        
        return score