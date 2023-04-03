"""
2023-03-31
https://school.programmers.co.kr/learn/courses/30/lessons/160585
혼자서 하는 틱택토
"""


def solution(board):
    wrong, o, x = is_wrong_turn(board)
    if wrong:
        return 0

    return is_end_condition(board, o, x)


def is_end_condition(board, o, x):
    line_list = [list(c) for c in board]
    winner_set = set()
    for j in range(len(board)):
        temp = []
        for i in range(len(board)):
            temp.append(board[i][j])
        line_list.append(temp)

    line_list.append([board[i][i] for i in range(len(board))])
    line_list.append([board[i][2 - i] for i in range(len(board))])

    for line in line_list:
        if end_condition(line):
            winner_set.add(line[0])

    if len(winner_set) == 2:
        return 0
    elif "O" in winner_set:
        return 1 if o - x == 1 else 0
    elif "X" in winner_set:
        return 1 if o == x else 0

    return 1


def end_condition(line):
    return line[0] == line[1] == line[2] and (line[0] != '.' and line[1] != '.' and line[2] != '.')


def is_wrong_turn(board):
    o, x = 0, 0
    for col in board:
        for row in col:
            if row == "O":
                o += 1
            elif row == "X":
                x += 1

    return not (0 <= o - x < 2), o, x
