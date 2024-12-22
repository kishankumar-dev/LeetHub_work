from heapq import *
class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:

        result = [-1] * len(queries)  

        qs = [[] for _ in range(len(heights))] 

        for index, (alice, bob) in enumerate(queries):

            if alice > bob:
                alice, bob = bob, alice

            if alice == bob or heights[alice] < heights[bob]:
                result[index] = bob
            else:
        
                qs[bob].append((heights[alice], index))  

        
        min_heap = []

        
        for index, height in enumerate(heights):
            
            for q in qs[index]:
                heappush(min_heap, q)
            
            while min_heap and min_heap[0][0] < height:
                _, query_index = heappop(min_heap)  
                result[query_index] = index  

        return result