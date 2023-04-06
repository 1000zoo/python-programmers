"""
2023-04-06
https://school.programmers.co.kr/learn/courses/30/lessons/118666
성격 유형 검사하기
"""


def solution(survey, choices):
    answer = ''
    nothing = 4
    result_dict = {}
    types = ["RT", "CF", "JM", "AN"]
    for ptype in types:
        for p in ptype:
            result_dict[p] = 0

    for s, c in zip(survey, choices):
        score = c - nothing
        ptype = s[0] if score < 0 else s[1]
        result_dict[ptype] += abs(score)

    for ptype in types:
        first, second = list(ptype)
        if result_dict[first] == result_dict[second]:
            answer += first if ord(first) < ord(second) else second
        else:
            answer += first if result_dict[first] > result_dict[second] else second

    return answer