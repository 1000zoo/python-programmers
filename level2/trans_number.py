"""
2023-03-21
https://school.programmers.co.kr/learn/courses/30/lessons/154538
숫자 변환하기
"""

def solution(x, y, n):
    dp = [-1 for _ in range(y + 1)]
    dp[x] = 0

    for i in range(x, y):
        if dp[i] == -1:
            continue

        if i + n <= y:
            dp[i + n] = dp[i] + 1 if dp[i + n] == -1 else min(dp[i + n], dp[i] + 1)

        if i * 2 <= y:
            dp[i * 2] = dp[i] + 1 if dp[i * 2] == -1 else min(dp[i * 2], dp[i] + 1)

        if i * 3 <= y:
            dp[i * 3] = dp[i] + 1 if dp[i * 3] == -1 else min(dp[i * 3], dp[i] + 1)

    return dp[y]

