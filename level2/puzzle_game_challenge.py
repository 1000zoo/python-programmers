"""
2024-09-11
https://school.programmers.co.kr/learn/courses/30/lessons/340212
퍼즐 게임 챌린지
"""

def solution(diffs, times, limit):
    left = 1
    right = max(diffs)

    while left < right:
        mid = (left + right) // 2

        if canSolve(mid, diffs, times, limit):
            right = mid
        else:
            left = mid + 1

    return left


def canSolve(level, diffs, times, limit):
    length = len(diffs)
    total_time = 0

    for i in range(length):
        diff_cur = diffs[i]
        time_cur = times[i]
        if i == 0:
            time_prev = 0
        else:
            time_prev = times[i - 1]

        total_time += doItAgain(diff_cur, level) * (time_prev + time_cur) + time_cur

    return total_time <= limit


def doItAgain(diff, level):
    ans = diff - level
    return ans if ans > 0 else 0

