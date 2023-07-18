"""
2023-07-18
https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3
같은 숫자는 싫어
"""

def solution(arr):
    prev = None
    answer = []
    for num in arr:
        if num != prev:
            answer.append(num)
            prev = num

    return answer
