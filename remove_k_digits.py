"""
Remove k digits: https://leetcode.com/problems/remove-k-digits/
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for n in num:
            while stack and k > 0 and n < stack[-1]:
                stack.pop()
                k -= 1

            stack.append(n)

        while k:
            stack.pop()
            k -= 1

        return ''.join(stack).lstrip('0') or '0'
