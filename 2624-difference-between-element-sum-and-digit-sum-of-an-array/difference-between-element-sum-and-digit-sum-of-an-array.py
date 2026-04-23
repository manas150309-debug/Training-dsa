class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_ = 0
        for x in nums:
            sum_ += x
            num = x
            while (num>0):
                sum_ -= (num%10)
                num = num//10
        return sum_