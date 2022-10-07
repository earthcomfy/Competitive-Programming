"""
Products of array: https://leetcode.com/problems/product-of-array-except-self/
"""
class Solution:
    # O(1) space complexity
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix = suffix = 1
        products = [1] * size
        
        for i in range(size):
            products[i] = prefix
            prefix *= nums[i]
        
        for i in range(size-1, -1, -1):
            products[i] *= suffix
            suffix *= nums[i]
        
        return products
    

    
#     O(n) space complexity
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         size = len(nums)
#         prefix = [1] * size
#         suffix = [1] * size
#         products = [1] * size
        
#         for i in range(1, size):
#             prefix[i] = prefix[i-1] * nums[i-1]
        
#         for i in range(size-2, -1, -1):
#             suffix[i] = suffix[i+1] * nums[i+1]
        
#         for i in range(size):
#             products[i] = prefix[i] * suffix[i]
        
        
#         return products
