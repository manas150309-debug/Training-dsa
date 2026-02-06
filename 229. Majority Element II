class Solution:
    def majorityElement(self, nums):
        # Step 1: setup
        c1 = c2 = None
        cnt1 = cnt2 = 0
        
        # Step 2: find possible answers
        for num in nums:
            if num == c1:
                cnt1 += 1
            elif num == c2:
                cnt2 += 1
            elif cnt1 == 0:
                c1 = num
                cnt1 = 1
            elif cnt2 == 0:
                c2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        # Step 3: verify
        ans = []
        n = len(nums)
        
        if nums.count(c1) > n // 3:
            ans.append(c1)
        if c2 != c1 and nums.count(c2) > n // 3:
            ans.append(c2)
        
        return ans
