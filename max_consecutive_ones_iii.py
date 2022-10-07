"""
Sliding window: https://leetcode.com/problems/max-consecutive-ones-iii/
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = zeroes = res = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes += 1
            
            while zeroes > k:
                if nums[l] == 0:
                    zeroes -= 1 
                l += 1
            
            res = max(res, r-l+1)
        
        return res
