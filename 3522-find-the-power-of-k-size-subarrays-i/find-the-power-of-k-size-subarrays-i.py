class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        m = n - k + 1
        arr = [0] * m
        
        # Calculating sum of first k-1 elements
        pre_sum = sum(nums[:k-1])

        idx = 0
        for i in range(n - k + 1):
            j = i + k - 1
            pre_sum += nums[j]  # Adding new element to sum
            
            if (k * (nums[i] + nums[i] + k - 1) // 2) == pre_sum and nums[i] <= nums[j]:
                arr[idx] = nums[j]
            else:
                arr[idx] = -1
            
            idx += 1
            pre_sum -= nums[i]  # Removing the i'th element for next iteration

        return arr