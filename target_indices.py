"""
Target Indices: https://leetcode.com/problems/find-target-indices-after-sorting-array/submissions/
"""
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [i for i in range(len(nums)) if nums[i] == target]
