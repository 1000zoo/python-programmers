"""
2024-05-01
https://school.programmers.co.kr/learn/courses/30/lessons/72411
메뉴 리뉴얼
"""

from itertools import combinations

def solution(orders, course):
    answer = []

    for i in course:
        temp = {}
        for order in orders:
            comb = combinations(order, i)
            for c in comb:
                c = sorted(c)
                menu = "".join(c)
                temp[menu] = temp.get(menu, 0) + 1

        ll = []
        temp = dict(sorted(temp.items(), key=lambda item: -item[1]))
        _max = None
        for key in temp.keys():
            if temp[key] <= 1:
                break
            if _max and temp[key] != _max or temp[key] <= 1:
                break
            _max = temp[key]
            ll.append(key)
        answer.extend(ll)

    return sorted(answer)