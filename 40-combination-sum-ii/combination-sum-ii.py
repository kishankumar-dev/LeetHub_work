class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.backtrack(result, [], candidates, target, 0)
        return result
    
    def backtrack(self, result: List[List[int]], current: List[int], candidates: List[int], remaining: int, start: int):
        if remaining < 0:
            return
        elif remaining == 0:
            result.append(list(current))
        else:
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                current.append(candidates[i])
                self.backtrack(result, current, candidates, remaining - candidates[i], i + 1)
                current.pop()