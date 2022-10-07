"""
Prefix sum: https://leetcode.com/problems/subarray-sum-equals-k/
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        left_sum = count = 0
        hashmap = {0:1}

        for i in range(len(nums)):
            left_sum += nums[i]

            if left_sum - k in hashmap:
                count += hashmap[left_sum-k]

            hashmap[left_sum] = hashmap.get(left_sum, 0) + 1

        return count
