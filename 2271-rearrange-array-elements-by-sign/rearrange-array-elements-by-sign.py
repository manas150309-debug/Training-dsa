class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        o=0
        p=[]
        ne=[]
        for i in nums:
            if i>0:
                p.append(i)
            else:
                ne.append(i)
        for j in range(0,n,2):
            nums[j]=p[o]
            nums[j+1]=ne[o]
            o+=1
        return nums