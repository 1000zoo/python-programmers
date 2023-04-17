"""
2023-04-17
https://school.programmers.co.kr/learn/courses/30/lessons/172928
공원 산책
"""

def solution(park, routes):
    answer = []
    H = len(park)
    W = len(park[0])
    dir_dict = {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}

    curr_pos = find_start(park)

    for route in routes:
        direction, count = route.split(" ")
        dh, dw = dir_dict[direction]
        count = int(count)
        tb = True
        nh, nw = curr_pos[0] + (dh * count), curr_pos[1] + (dw * count)

        if not check_boundary(H, W, (nh, nw)):
            continue

        for c in range(count + 1):
            if cant_go(park, (curr_pos[0] + dh * c, curr_pos[1] + dw * c)):
                tb = False
                break

        if tb:
            curr_pos = (nh, nw)

    return curr_pos


def find_start(park):
    for i, h in enumerate(park):
        for j, w in enumerate(h):
            if w == 'S':
                return (i, j)

    return None


def cant_go(park, pos):
    return park[pos[0]][pos[1]] == 'X'


def check_boundary(h, w, pos):
    return 0 <= pos[0] < h and 0 <= pos[1] < w
