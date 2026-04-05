class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1
        nums.clear()
        for i in f.keys():
            nums.append(i)
        return len(nums)
        