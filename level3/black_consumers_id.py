"""
2023-08-20
https://school.programmers.co.kr/learn/courses/30/lessons/64064
불량사용자
"""

def solution(user_id, banned_id):
    possible = [[] for _ in range(len(banned_id))]

    for i, ban in enumerate(banned_id):
        for user in user_id:
            if poss(user, ban):
                possible[i].append(user)

    answers = set()


    ## 여러 선택지들 중에서 가능한 모든 경우의수를 뽑아낸다.
    def dfs(idx, selected):
        if idx == len(banned_id):
            answers.add(tuple(sorted(selected)))
            return

        for user in possible[idx]:
            if user not in selected:
                dfs(idx + 1, selected + [user])

    dfs(0, [])

    return len(answers)


def poss(user, ban):
    if len(user) != len(ban):
        return False

    for i in range(len(ban)):
        if user[i] != ban[i] and ban[i] != '*':
            return False

    return True
