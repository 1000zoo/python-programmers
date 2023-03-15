"""
2023-03-15
https://school.programmers.co.kr/learn/courses/30/lessons/155652?language=python3
둘만의 암호
"""

def solution(s, skip, index):
    answer = ''

    char_set = []
    for i in range(26):
        temp = chr(i + ord('a'))
        if not temp in skip:
            char_set.append(temp)

    print(char_set)

    for alp in s:
        new_index = char_set.index(alp) + index
        new_index = new_index if new_index < len(char_set) else new_index % len(char_set)
        answer += char_set[new_index]

    return answer
