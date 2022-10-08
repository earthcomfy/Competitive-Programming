"""
Rotate array: https://leetcode.com/problems/rotate-array/
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        copy = list(nums)
        
        for i in range(size):
            nums[(i + k) % size] = copy[i];
