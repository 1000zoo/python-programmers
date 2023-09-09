"""
2023-09-09
https://school.programmers.co.kr/learn/courses/30/lessons/42890?language=python3
후보키
"""

from itertools import combinations

def solution(relation):
    tl = [i for i in range(len(relation[0]))]

    comb = []
    for i in range(1, len(tl) + 1):
        comb = comb + list(combinations(tl, i))

    candidate_set = set()

    for com in comb:
        temp = ["" for _ in range(len(relation))]

        for c in com:
            temp = sum_attr(temp, get_attr(relation, c))

        if is_unique(temp) and check_minimality(candidate_set, com):
            candidate_set.add(com)

    return len(candidate_set)


def part_of(com1, com2):
    check = False
    for c1 in com1:
        for c2 in com2:
            check = c1 == c2
            if check:
                break
        if not check:
            return False

    return True


def check_minimality(_set, _comb):
    if len(_set) == 0:
        return True

    for s in _set:
        if part_of(s, _comb):
            return False

    return True


def sum_attr(attr1, attr2):
    return [attr1[i] + " " + attr2[i] for i in range(len(attr1))]


def get_attr(r, i):
    return [r[a][i] for a in range(len(r))]


def is_unique(attr):
    s = set(attr)
    return len(s) == len(attr)
