"""
2023-03-22
https://school.programmers.co.kr/learn/courses/30/lessons/138477
명예의 전당 (1)
"""

from queue import PriorityQueue

def solution(k, score):
    answer = []
    pq = PriorityQueue()

    for s in score:

        if pq.qsize() < k:
            pq.put(s)
        else:
            if s > pq.queue[0]:
                pq.get()
                pq.put(s)

        answer.append(pq.queue[0])

    return answer


pq1 = PriorityQueue()
pq1.put(3)
pq1.put(2)
pq1.put(1)

print(pq1.qsize())