class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sort_ind = sorted(range(len(nums)), key = lambda i: nums[i])
        left, prev, ans = 0, nums[sort_ind[0]], nums.copy()
        for right, ind in enumerate(sort_ind + [-1]):
            if ind == -1 or nums[ind] - prev > limit:
                for i, j in zip(sort_ind[left:right], sorted(sort_ind[left:right])):
                    ans[j] = nums[i]
                left = right
            prev = nums[ind]    
        return ans