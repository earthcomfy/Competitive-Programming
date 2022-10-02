"""
Selection Sort: https://practice.geeksforgeeks.org/problems/selection-sort/1
"""
class Solution: 
    def selectionSort(self, arr,n):
        for i in range(n):
            min_index = i
            
            for j in range(i+1, n):
                if arr[min_index] > arr[j]:
                    min_index = j
            
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp
