"""
2023-03-22
https://school.programmers.co.kr/learn/courses/30/lessons/142086
가장 가까운 같은 글자
"""

def solution(s):
    answer = []
    alp_map = {}

    for i, alp in enumerate(s):
        if alp in alp_map.keys():
            answer.append(i - alp_map[alp])
        else:
            answer.append(-1)
        alp_map[alp] = i


    return answer
