"""
2023-07-18
https://school.programmers.co.kr/learn/courses/30/lessons/68935?language=python3
3진법 뒤집기
"""

def solution(n):
    answer = 0
    while n != 0:
        answer *= 3
        answer += (n % 3)
        n //= 3
    return answer
