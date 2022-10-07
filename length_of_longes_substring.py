"""
Sliding window: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Using set so that add and remove operations can be faster
        l = res = 0
        chars = set()

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1

            chars.add(s[r])
            res = max(res, r-l+1)

        return res
    
      
    
    
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         l = res = 0
#         hashmap = {}

#         for r in range(len(s)):
#             while s[r] in hashmap:
#                 hashmap.pop(s[l])
#                 l += 1

#             hashmap[s[r]] = 1
#             res = max(res, r-l+1)

#         return res
