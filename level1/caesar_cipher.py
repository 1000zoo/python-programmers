"""
2023-07-26
https://school.programmers.co.kr/learn/courses/30/lessons/12926?language=python3
시저 암호
"""


def solution(s, n):
    return ''.join(list(map(lambda c: chr(((ord(c) + n - ord('a')) % 26) + ord('a')) if c.islower()
    else chr(((ord(c) + n - ord('A')) % 26) + ord('A')) if c.isupper()
    else ' '
                            , s)))
