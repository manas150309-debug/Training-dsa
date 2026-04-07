class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       n=len(nums)
       h={}
       l=[]
       for i in range(n):
        rem=target-nums[i]
        if rem in h:
            l.append (h[rem])
            l.append (i)
            return l
        h[nums[i]]=i