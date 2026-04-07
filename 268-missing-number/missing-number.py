class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # if max(nums)==len(nums)+1:
        #     return 
        # c=0
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         c=i
        # return c
        # h={}
        # for i in range(len(nums)+1):
        #     h[i]=0
        # for j in nums:
        #     h[j]=1
            
        # for k,v in h.items():
        #     if v==0:
        #         return k

        n=len(nums)
        expected_sum=n*(n+1)//2
        actual=sum(nums)
        return expected_sum-actual