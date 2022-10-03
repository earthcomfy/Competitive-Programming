"""
Valide stack sequences: https://leetcode.com/problems/validate-stack-sequences/
"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        ptr = 0

        if pushed == popped:
            return True

        else:
            for i in pushed:
                stack.append(i)

                while ptr < len(popped) and stack[-1] == popped[ptr]:
                    stack.pop()
                    ptr += 1

                    if not stack:
                        break

            return stack == []
 
