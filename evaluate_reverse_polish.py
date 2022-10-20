"""
Reverse Polish: https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""
class Solution:
    def evaluate(self, x: int, y: int, operator: str) -> int:
        if operator == '+':
            return x + y
        if operator == '-':
            return x - y
        if operator == '*':
            return x * y
        return int(x * 1.0 / y)
        
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(('+', '-', '*', '/'))
        
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()
                
                res = self.evaluate(x, y, token)
                stack.append(res)
        
        return stack[-1]              
  
