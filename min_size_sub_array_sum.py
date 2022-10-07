"""
Minimum sub-array length: https://leetcode.com/problems/minimum-size-subarray-sum/
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = l = 0
        res = len(nums) + 1
        
        for r in range(len(nums)):
            total += nums[r]
            
            while total >= target:
                res = min(res, r-l+1)
                total -= nums[l]
                l += 1
            

        return res if res <= len(nums) else 0
