"""
2023-03-17
https://school.programmers.co.kr/learn/courses/30/lessons/154540
무인도 여행
"""

def solution(maps):
    answer = []
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    queue = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] ## 상 하 좌 우
    boundary = (len(maps), len(maps[0]))

    for i, col in enumerate(maps):
        for j, row in enumerate(col):
            curr = (i, j)
            if visited[i][j]:
                continue
            if _is_island(row):
                queue.append(curr)
                temp = 0
                while queue:
                    pos = queue.pop(0)
                    visited[pos[0]][pos[1]] = True
                    temp += int(maps[pos[0]][pos[1]])

                    for d in directions:
                        next_sq = (pos[0] + d[0], pos[1] + d[1])
                        if not _check_boundary(next_sq, boundary):
                            continue
                        if not _is_island(maps[next_sq[0]][next_sq[1]]):
                            continue
                        if not visited[next_sq[0]][next_sq[1]] and not next_sq in queue:
                            queue.append(next_sq)

                answer.append(temp)
    answer.sort()
    if not answer:
        answer = [-1]
    return answer

def _check_boundary(sq, boundary):
    i, j = sq
    i_max, j_max = boundary
    return 0 <= i < i_max and 0 <= j < j_max

def _is_island(sq):
    return sq != 'X'
