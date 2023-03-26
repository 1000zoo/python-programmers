"""
2023-03-26
https://school.programmers.co.kr/learn/courses/30/lessons/72410
신규 아이디 추천
"""


def solution(new_id):
    new_id = _step1(new_id)
    new_id = _step2(new_id)
    new_id = _step3(new_id)
    new_id = _step4(new_id)
    new_id = _step5(new_id)
    new_id = _step6(new_id)
    new_id = _step7(new_id)
    return new_id

def _step1(id):
    return id.lower()

def _step2(id):
    temp = ""
    for c in id:
        if _is_valid_char(c):
            temp += c
    return temp

def _step3(id):
    dot = False
    temp = ""

    for c in id:
        if c == '.':
            if not dot:
                temp += c
                dot = True
        else:
            temp += c
            dot = False

    return temp

def _step4(id):
    return id.strip('.')

def _step5(id):
    return id if id else 'a'

def _step6(id):
    if len(id) > 15:
        id = id[:15]
    return _step4(id)

def _step7(id):
    while len(id) < 3:
        id += id[-1]
    return id


def _is_valid_char(c):
    return _is_alp(c) or _is_num(c) or _is_etc(c)

def _is_alp(c):
    return ord('a') <= ord(c) <= ord('z')

def _is_num(c):
    return ord('0') <= ord(c) <= ord('9')

def _is_etc(c):
    return c == '-' or c == '_' or c == '.'

