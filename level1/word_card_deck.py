"""
2023-03-14
https://school.programmers.co.kr/learn/courses/30/lessons/159994
카드뭉치
"""

def solution(cards1, cards2, goal):
    while goal:
        if cards1 and goal[0] == cards1[0]:
            cards1.pop(0)
            goal.pop(0)
            continue

        else:
            if cards2 and goal[0] == cards2[0]:
                cards2.pop(0)
                goal.pop(0)
                continue
            else:
                return "No"

    return "Yes"
