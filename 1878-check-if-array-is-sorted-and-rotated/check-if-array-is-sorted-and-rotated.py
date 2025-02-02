class Solution:
    def check(self, nums: List[int]) -> bool:
        n, rotations = len(nums), 0
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]: # check adj numbers, % n to compare [last, first]
                rotations += 1 # found a rotation
                if rotations > 1: 
                    return False # found more than 1 rotation
        
        return True # didn't find more than 1 rotation