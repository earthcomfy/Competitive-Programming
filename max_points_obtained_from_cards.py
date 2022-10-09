"""
Sliding window: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
"""
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints[:k])
        n = len(cardPoints)
        res = total
        l = 1

        while l <= k:
            total +=  cardPoints[n-l] - cardPoints[k-l]
            res = max(res, total)
            l += 1

        return res
