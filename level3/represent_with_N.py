"""
2024-04-02
https://school.programmers.co.kr/learn/courses/30/lessons/42895
N으로 표현
"""

def solution(N, number):
    if N == number:
        return 1
    set_list = [{N}]

    while len(set_list) < 8:
        curr_index = len(set_list) + 1
        new_set = {int(str(N) * curr_index)}  # curr_index 번 사용해서 만들 수 있는 모든 중복없는 수들
        for i in range(1, curr_index):
            j = curr_index - i
            set_i = set_list[i - 1]
            set_j = set_list[j - 1]
            for n in set_i:
                for m in set_j:
                    all_calculate(new_set, n, m)

        if number in new_set:
            return curr_index

        set_list.append(new_set)

    return -1


def all_calculate(_set: set, a: int, b: int):
    _set.add(a + b)
    _set.add(a - b)
    _set.add(a * b)
    if b != 0:
        _set.add(a // b)