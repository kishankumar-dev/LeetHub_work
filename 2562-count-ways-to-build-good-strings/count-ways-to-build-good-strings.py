class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        self.low = low
        self.high = high
        self.zero = zero
        self.one = one

        return self.findWaysToBuild(0)

    @cache
    def findWaysToBuild(self, existing_len):
        if existing_len > self.high:
            return 0

        good_str = 0
        if existing_len >= self.low:
            good_str += 1
     
        good_str += self.findWaysToBuild(existing_len + self.zero)
     
        good_str += self.findWaysToBuild(existing_len + self.one)
        return good_str % 1000000007
            