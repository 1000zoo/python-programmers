"""
2023-09-01
https://school.programmers.co.kr/learn/courses/30/lessons/64062?language=python3#
징검다리 건너기
"""

from collections import deque

def solution(stones, k):
    answer = 1e12
    q = deque()

    for i, stone in enumerate(stones):
        while len(q) != 0 and q[-1][1] < stone:
            q.pop()
        q.append((i, stone))

        if i - q[0][0] >= k:
            q.popleft()

        if i >= k - 1:
            answer = min(answer, q[0][1])

    return answer