"""
2023-04-05
https://school.programmers.co.kr/learn/courses/30/lessons/159993#
미로 탈출
"""

def solution(maps):
    sx, sy = findXY("S", maps)
    ls, ly = findXY("L", maps)
    ex, ey = findXY("E", maps)

    start_to_lever = short_distance((sx, sy), (ls, ly), maps)
    lever_to_end = short_distance((ls, ly), (ex, ey), maps)

    if start_to_lever != -1 and lever_to_end != -1:
        return start_to_lever + lever_to_end

    return -1

def short_distance(start, end, maps):
    dp = [[-1 for _ in maps[0]] for _ in maps]
    x, y = start
    ex, ey = end
    dp[x][y] = 0

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = [start]

    while queue:
        curr = queue.pop(0)
        x, y = curr

        for d in directions:
            nx, ny = x + d[0], y + d[1]

            if not in_boundary((nx, ny), maps) or not can_go((nx, ny), maps):
                continue

            if dp[nx][ny] == -1 or dp[nx][ny] > dp[x][y] + 1:
                queue.append((nx, ny))
                dp[nx][ny] = dp[x][y] + 1

    return dp[ex][ey]



def can_go(curr, maps):
    return maps[curr[0]][curr[1]] != "X"

def in_boundary(curr, maps):
    return 0 <= curr[0] < len(maps) and 0 <= curr[1] < len(maps[0])

def findXY(c, maps):
    for i, line in enumerate(maps):
        for j, sq in enumerate(line):
            if sq == c:
                return i, j
