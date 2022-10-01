"""
Counting Sort: https://www.hackerrank.com/challenges/countingsort1/problem
"""
def countingSort(arr):
    counting_arr = [0] * 100
    
    for i in range(len(arr)):
        counting_arr[arr[i]] += 1
    
    return counting_arr
