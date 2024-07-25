class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(array):
            if len(array) <= 1:
                return array
            
            middle = len(array)//2
            left = mergeSort(array[:middle])
            right = mergeSort(array[middle:])

            temp = []
            while left or right:
                if left and right:
                    if left[0] < right[0]:
                        temp.append(left.pop(0))
                    else:
                        temp.append(right.pop(0))
                else:
                    if left:
                        temp.append(left.pop(0))
                    if right:
                        temp.append(right.pop(0))

            return temp

        return mergeSort(nums)

        