"""
2023-07-26
https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=python3
최소 직사각형
"""

def solution(sizes):
    return max([max(x) for x in sizes]) * max([min(x) for x in sizes])

