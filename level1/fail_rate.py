"""
2023-08-22
https://school.programmers.co.kr/learn/courses/30/lessons/42889?language=python3
실패율
"""

def solution(N, stages):
    info = {}

    for i in range(1, N + 1):
        total = 0
        fail = 0
        for s in stages:
            total += 1 if s >= i else 0
            fail += 1 if s == i else 0

        info[i] = 0 if total == 0 else fail / total

    return sorted(info, key=lambda x: -info[x])