"""
2023-03-26
https://school.programmers.co.kr/learn/courses/30/lessons/135808
과일 장수
"""

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    lst = [i * m for i in range(len(score) // m)]

    for index in lst:
        price = score[index]
        for i in range(m):
            price = min(price, score[i + index])
        answer += price * m

    return answer


k = solution(3,	4,	[1, 2, 3, 1, 2, 3, 1])
print(k)