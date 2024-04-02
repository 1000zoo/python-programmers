"""
2024-04-02
https://school.programmers.co.kr/learn/courses/30/lessons/42626?language=python3
더 맵게
"""

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 1:
        if scoville[0] >= K:
            return answer

        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + 2 * b)

        answer += 1

    return answer if scoville[0] >= K else -1
