"""
Stack - Valid Parentheses: https://leetcode.com/problems/valid-parentheses/submissions/
"""
class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': ')', '[': ']', '{': '}'}
    
        if len(s) %2 != 0:
            return False

        stack = []

        for i in s:
            if i in d.keys():
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False

                if d[stack.pop()] != i:
                    return False

        return len(stack) == 0
        
