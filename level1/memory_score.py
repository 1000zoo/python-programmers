"""
2023-04-17
https://school.programmers.co.kr/learn/courses/30/lessons/176963
추억 점수
"""

from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    scores = defaultdict(lambda: 0)

    for i, person in enumerate(name):
        scores[person] = yearning[i]

    for p in photo:
        temp = 0
        for person in p:
            temp += scores[person]
        answer.append(temp)

    return answer