"""
2023-08-08
https://school.programmers.co.kr/learn/courses/30/lessons/17681
비밀지도
"""

def solution(n, arr1, arr2):
    return ["".join(['#' if m == "1" else " "for m in format(a|b, 'b').rjust(n, '0')]) for a, b in zip(arr1, arr2)]

