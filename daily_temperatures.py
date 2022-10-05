"""
Daily temperatures: https://leetcode.com/problems/daily-temperatures/
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        stack = []
        res = [0 for _ in range(size)]

        for t in range(size):
            while stack and temperatures[t] > temperatures[stack[-1]]:
                i = stack.pop()
                res[i] = t - i

            stack.append(t)

        return res
