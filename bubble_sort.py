"""
Bubble Sort: https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
"""
def count_swaps(a):
    size = len(a)
    number_of_swaps = 0
    temp = None
    
    for i in range(size):
        for j in range(size-1):
            if (a[j] > a[j+1]):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                number_of_swaps += 1
    
    print(f'Array is sorted in {number_of_swaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
