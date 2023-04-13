"""
2023-04-13
https://school.programmers.co.kr/learn/courses/30/lessons/181188
요격 시스템
"""

def solution(targets):
    answer = 0
    end = 0
    targets.sort(key=lambda x : (x[0], x[1]))

    for target in targets:
        ns, ne = target

        if ns >= end:
            answer += 1
            end = ne
        else:
            end = min(ne, end)

    return answer
