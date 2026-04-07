from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        temp = []
        
        # Step 1: Store non-zero elements
        for i in nums:
            if i != 0:
                temp.append(i)
        
        # Step 2: Fill original array
        n = len(nums)
        t = len(temp)
        
        for i in range(t):
            nums[i] = temp[i]
        
        # Step 3: Fill remaining with zeros
        for i in range(t, n):
            nums[i] = 0