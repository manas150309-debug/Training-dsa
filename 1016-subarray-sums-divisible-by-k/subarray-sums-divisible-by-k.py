class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        count = 0
        rem_map = {0: 1}  # important for subarrays starting from index 0
        
        for num in nums:
            prefixSum += num
            rem = prefixSum % k
            
            # handle negative remainder
            if rem < 0:
                rem += k
            
            if rem in rem_map:
                count += rem_map[rem]
            
            rem_map[rem] = rem_map.get(rem, 0) + 1
        
        return count