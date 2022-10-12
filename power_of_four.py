"""
https://leetcode.com/problems/power-of-four/
"""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        return (math.log10(n) / math.log10(4)) % 1 == 0