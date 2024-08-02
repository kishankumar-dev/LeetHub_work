class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count_ones = nums.count(1)
        if count_ones == 0:
            return 0

        # Extend the array to handle the circular nature
        extended_nums = nums + nums

        # Initialize the number of zeroes in the first window
        current_zeroes = extended_nums[:count_ones].count(0)
        min_zeroes = current_zeroes

        # Slide the window
        for i in range(count_ones, len(extended_nums)):
            if extended_nums[i] == 0:
                current_zeroes += 1
            if extended_nums[i - count_ones] == 0:
                current_zeroes -= 1

            min_zeroes = min(min_zeroes, current_zeroes)

        return min_zeroes

# Test the solution
sol = Solution()
nums = [1, 0, 1, 0, 1, 0, 0, 1]
print(sol.minSwaps(nums))  # Expected output should consider the circular nature