"""
2023-03-23
https://school.programmers.co.kr/learn/courses/30/lessons/138476
귤 고르기
"""

def solution(k, tangerine):
    answer = 0
    numbers = {}

    for size in tangerine:
        if size in numbers.keys():
            numbers[size] += 1
        else:
            numbers[size] = 1

    key_list = list(numbers.keys())
    key_list = sorted(key_list, key=lambda x : numbers[x], reverse=True)

    count = 0

    for key in key_list:
        answer += 1
        count += numbers[key]
        if count >= k:
            break

    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))