"""
2024-05-01
https://school.programmers.co.kr/learn/courses/30/lessons/42578
의상
"""

def solution(clothes):
    dd = {}

    for c in clothes:
        item = c[0]
        category = c[1]
        if not category in dd.keys():
            dd[category] = [None]
        dd[category].append(item)

    answer = 1
    for key in dd.keys():
        answer *= len(dd[key])

    return answer - 1
