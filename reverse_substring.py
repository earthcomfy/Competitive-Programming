"""
Reverse substring: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
"""
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
    
        for i in s:
            if i != ')':
                stack.append(i)

            else:
                substr = ''
                
                while stack:
                    val = stack.pop()
                    
                    if val == '(':
                        break
                    else:
                        substr += val[::-1]

                stack.append(substr)
        
        return ''.join(stack)
