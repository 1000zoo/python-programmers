"""
2024-09-13
https://school.programmers.co.kr/learn/courses/30/lessons/12913
땅따먹기
"""

def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            temp = land[i][j]
            for k in range(len(land[0])):
                if j == k:
                    continue
                land[i][j] = max(temp + land[i - 1][k], land[i][j])

    return max(land[-1])