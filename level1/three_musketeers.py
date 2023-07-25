"""
2023-07-26
https://school.programmers.co.kr/learn/courses/30/lessons/131705
삼총사
"""

def short(number):
    from itertools import combinations
    return len([lst for lst in combinations(number, 3) if sum(lst) == 0])

def solution(number):
    return dfs(number, [], 0, 0)

def dfs(number, curr_list, curr_index, answer):
    if len(curr_list) == 3:
        return answer if sum(curr_list) != 0 else answer + 1

    temp = curr_list.copy()
    for i in range(curr_index, len(number)):
        temp.append(number[i])
        answer = dfs(number, temp, i + 1, answer)
        temp.pop()

    return answer
