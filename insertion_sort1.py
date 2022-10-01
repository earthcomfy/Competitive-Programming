"""
Insertion Sort1: https://www.hackerrank.com/challenges/insertionsort1/problem
"""
def insertionSort1(n, arr):
    unsorted_elem = arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i] > unsorted_elem:
            arr[i+1] = arr[i]
            print(*arr)
        else:
            arr[i+1] = unsorted_elem
            print(*arr)
            break
    
    if arr[0] > unsorted_elem:
        arr[0] = unsorted_elem
        print(*arr)
