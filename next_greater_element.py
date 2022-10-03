"""
Next greater element: https://leetcode.com/problems/next-greater-element-i/
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]: 
        stack = []

        for i in range(len(nums1)):
            flag = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    flag = True
                if flag and nums2[j] > nums1[i]:
                    stack.append(nums2[j])
                    flag = False
                    break

            if flag:
                stack.append(-1)

        return stack
