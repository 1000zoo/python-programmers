"""
2023-08-17
https://school.programmers.co.kr/learn/courses/30/lessons/12939?language=python3
최대값과 최솟값
"""

def solution(s):
    return str(min(map(int, s.split(" ")))) + " "  + str(max(map(int, s.split(" "))))
