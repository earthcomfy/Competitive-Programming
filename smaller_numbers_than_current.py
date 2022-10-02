"""
Smaller numbers than current: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/
"""
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_list = sorted(nums)
        d = {}

        for i in range(len(sorted_list)):
            if sorted_list[i] not in d:
                d[sorted_list[i]] = i

        return [d[num] for num in nums]
