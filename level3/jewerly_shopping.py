"""
2023-08-31
https://school.programmers.co.kr/learn/courses/30/lessons/67258?language=python3
보석쇼핑
"""

from collections import defaultdict

def solution(gems):
    answer = [0, len(gems)]
    typeSize = len(set(gems))
    table = defaultdict(int)

    s, e = 0, -1
    s_turn = False

    while (s != e) or (s != len(gems)):
        if s_turn:
            table[gems[s]] -= 1
            if table[gems[s]] == 0:
                del table[gems[s]]
            s += 1
        else:
            e += 1
            if e == len(gems):
                break

            table[gems[e]] += 1

        if len(table) < typeSize:
            s_turn = False

        elif len(table) == typeSize:
            if answer[1] - answer[0] > e - s:
                answer = [s + 1, e + 1]
            s_turn = True

    return answer