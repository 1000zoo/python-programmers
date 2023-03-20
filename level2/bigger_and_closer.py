"""
2023-03-20
https://school.programmers.co.kr/learn/courses/30/lessons/154539
뒤에 있는 큰 수 찾기
"""
from queue import PriorityQueue

def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    pq = PriorityQueue()

    for i, num in enumerate(numbers):
        pq.put((num, i))
        while pq.queue[0][0] < num:
            answer[pq.queue[0][1]] = num
            pq.get()


    return answer

