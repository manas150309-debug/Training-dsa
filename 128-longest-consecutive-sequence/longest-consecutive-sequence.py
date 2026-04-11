class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set=set (nums)
        count=0
        largest=0

        for i in my_set:
            if i-1 not in my_set:
                count=1
                while i+1  in my_set:
                    count+=1
                    i+=1
            largest=max(count,largest)
    
        return largest
