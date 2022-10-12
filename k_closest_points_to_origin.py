"""
Sorting: https://leetcode.com/problems/k-closest-points-to-origin/
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:  
#         res = []
        
#         for i in range(len(points)):
#             x1 = points[i][0]
#             y1 = points[i][1]
            
#             d = (x1)**2 + (y1)**2
#             res.append([x1, y1, d])
        
#         res.sort(key=lambda x:x[2])
        
#         return [i[:-1] for i in res[:k]]
    
        return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]
