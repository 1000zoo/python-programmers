"""
2024-05-01
https://school.programmers.co.kr/learn/courses/30/lessons/17677
뉴스 클러스터링
"""

def solution(str1, str2):
    intersection = get_intersection(get_set(str1), get_set(str2))
    union = get_union(get_set(str1), get_set(str2))

    if not union:
        return 65536
    return int(65536 * len(intersection) / len(union))

def get_intersection(set1, set2):
    intersection = []
    set1.sort()
    set2.sort()

    while set1 and set2:
        if set1[0] == set2[0]:
            intersection.append(set1.pop(0))
            set2.pop(0)
        elif set1[0] < set2[0]:
            set1.pop(0)
        elif set1[0] > set2[0]:
            set2.pop(0)

    return intersection


def get_union(set1, set2):
    union = []
    set1.sort()
    set2.sort()

    while set1 or set2:
        if not set1:
            union.append(set2.pop(0))
            continue
        if not set2:
            union.append(set1.pop(0))
            continue
        if set1[0] == set2[0]:
            union.append(set1.pop(0))
            set2.pop(0)
        elif set1[0] < set2[0]:
            union.append(set1.pop(0))
        else:
            union.append(set2.pop(0))

    return union

def get_set(s):
    s = s.lower()
    result = []
    for i in range(len(s) - 1):
        if not (s[i].islower() and s[i + 1].islower()):
            continue
        result.append(s[i] + s[i + 1])
    return result
