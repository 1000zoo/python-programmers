"""
//2023-04-18
//https://school.programmers.co.kr/learn/courses/30/lessons/181187
//두 원 사이의 정수 쌍
"""

import math

def solution(r1, r2):
    answer = 0
    for x in range(1, r2 + 1):
        y1 = 0 if r1 < x else math.ceil(get_y(r1, x))
        y2 = math.floor(get_y(r2, x))
        answer += (y2 - y1 + 1)

    return answer * 4

def get_y(r, x):
    return math.sqrt(r ** 2 - x ** 2)
