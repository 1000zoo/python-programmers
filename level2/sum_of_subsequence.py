"""
2023-04-12
https://school.programmers.co.kr/learn/courses/30/lessons/178870
연속된 부분 수열의 합
"""

def solution(sequence, k):
    answer = []
    minLength = float('inf')
    _sum = 0
    start = end = 0

    while True:
        if end == len(sequence) and _sum < k:
            break

        if _sum == k:
            if end - start + 1 < minLength:
                minLength = end - start + 1
                answer = [start, end - 1]

        if end < len(sequence) and _sum < k:
            _sum += sequence[end]
            end += 1
        elif start < len(sequence):
            _sum -= sequence[start]
            start += 1

    return answer