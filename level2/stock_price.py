"""
2024-09-13
https://school.programmers.co.kr/learn/courses/30/lessons/42584
주식가격
"""

def solution(prices):
    answer = [i for i in range(len(prices) - 1, -1, -1)]
    stack = []

    for i in range(len(prices) - 1):
        stack.append(i)
        while stack and prices[stack[-1]] > prices[i + 1]:
            last_index = stack.pop()
            answer[last_index] = (i + 1) - last_index

    return answer
