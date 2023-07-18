"""
2023-07-18
https://school.programmers.co.kr/learn/courses/30/lessons/12930?language=python3
이상한 문자 만들기
"""

def solution(s):
    sp = s.split(' ')
    temp = []
    for word in sp:
        temp.append(wierd_word(word))
    return ' '.join(temp)

def wierd_word(s):
    temp = ''
    for i, c in enumerate(s):
        temp += c.upper() if i % 2 == 0 else c.lower()
    return temp
