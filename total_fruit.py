"""
Sliding window: https://leetcode.com/problems/fruit-into-baskets/ 
"""
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_set = Counter()
        res = l = types = 0

        for r in range(len(fruits)):
            if fruit_set[fruits[r]] == 0:
                types += 1

            while types > 2:
                fruit_set[fruits[l]] -= 1
                if fruit_set[fruits[l]] == 0:
                    types -= 1
                l += 1

            fruit_set[fruits[r]] += 1
            res = max(res, r-l+1)

        return res
