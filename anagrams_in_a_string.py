"""
Sliding window: https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        s_count = Counter(s[:len(p)])
        res = []
        
        for i in range(0, len(s)-len(p)+1):  
            if s_count == p_count:
                res.append(i)
            
            s_count[s[i]] -= 1
            
            if s_count[s[i]] == 0:
                s_count.pop(s[i])
            
            if i + len(p) < len(s):
                s_count[s[i+len(p)]] += 1
        
        return res
        
        
        
