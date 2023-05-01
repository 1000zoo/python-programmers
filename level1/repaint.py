"""
2023-05-01
https://school.programmers.co.kr/learn/courses/30/lessons/161989
덧칠하기
"""

def solution(n, m, section):
    answer = 0
    index = 0

    while index < len(section):
        temp = section[index] + m

        while index < len(section):
            if section[index] < temp:
                index += 1
            else:
                break
        answer += 1

    return answer