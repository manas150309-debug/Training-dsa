class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if max(nums)==len(nums)+1:
            return 
        c=0
        for i in range(len(nums)+1):
            if i not in nums:
                c=i
        return c

        