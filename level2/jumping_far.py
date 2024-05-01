"""
2024-05-01
https://school.programmers.co.kr/learn/courses/30/lessons/12914
멀리뛰기
"""

def solution(n):
    if n <= 2:
        return n
    f1 = 1
    f2 = 2
    answer = 0
    for i in range(3, n + 1):
        answer = (f1 + f2) % 1234567
        f1 = f2
        f2 = answer
    return answer