"""
2024-09-13
https://school.programmers.co.kr/learn/courses/30/lessons/49993
스킬트리
"""

def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        queue = list(skill)
        flag = True
        for t in tree:
            if not queue:
                break
            if t == queue[0]:
                queue.pop(0)
                continue
            if t in queue:
                flag = False
                break
        if flag:
            answer += 1

    return answer
