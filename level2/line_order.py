"""
2024-05-03
https://school.programmers.co.kr/learn/courses/30/lessons/12936
줄 서는 방법
"""

def solution(n, k):
    answer = []
    l = [i for i in range(1, n + 1)]
    target = k - 1
    while l:
        n -= 1
        f = fact(n)
        index = target // f
        answer.append(l.pop(index))
        target %= f

    return answer

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)