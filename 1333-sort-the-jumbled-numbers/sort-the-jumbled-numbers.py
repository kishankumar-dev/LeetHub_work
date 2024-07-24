class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_with_index = []
        for index, num in enumerate(nums):
            mapped_num = mapping[0] if num == 0 else 0
            power_of_ten = 1
            while num:
                num, digit = divmod(num, 10)
                mapped_num = mapping[digit] * power_of_ten + mapped_num
                power_of_ten *= 10
            mapped_with_index.append((mapped_num, index))
        mapped_with_index.sort()
        return [nums[i] for _, i in mapped_with_index]