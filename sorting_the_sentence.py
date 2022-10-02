"""
Sorting the sentence: https://leetcode.com/problems/sorting-the-sentence/submissions/
"""
class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        words.sort(key=lambda word:word[-1])
        
        return ' '.join([word[:-1] for word in words])
