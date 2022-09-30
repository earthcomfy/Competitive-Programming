"""
Domino piling: https://codeforces.com/problemset/problem/50/A
"""

def get_maximal_number_of_dominoes(m, n):
    return (m * n) // 2

m, n = map(int, input().split(' '))
print(get_maximal_number_of_dominoes(m, n))
