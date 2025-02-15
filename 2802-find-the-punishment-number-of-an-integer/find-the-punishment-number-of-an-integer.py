class Solution:
    def punishmentNumber(self, n: int) -> int:

        def bt(partition, target):
            if partition < target:
                return False
            if not partition:
                return True
            new_partition, mod = partition, 10
            while new_partition:
                new_partition, num = divmod(partition, mod)
                if num <= target and bt(new_partition, target - num):
                    return True
                mod *= 10
            return False

        return sum(i*i for i in range(n+1) if bt(i*i, i))