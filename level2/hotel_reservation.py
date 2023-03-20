"""
2023-03-16
https://school.programmers.co.kr/learn/courses/30/lessons/155651
호텔 대실
"""

def solution(book_time : list):
    answer = 0
    book_time.sort(key=lambda x : (x[0], x[1]))
    times = []
    room = []

    for bt in book_time:
        times.append(_decode(bt))

    for time in times:
        while room and room[0][1] <= time[0]:
            room.pop(0)

        room.append(time)
        room.sort(key=lambda x : (x[1]))
        print(room)
        answer = max(answer, len(room))

    return answer

def _decode(time):
    start, end = time
    s = int(start.split(":")[0]) * 60 + int(start.split(":")[1])
    e = int(end.split(":")[0]) * 60 + int(end.split(":")[1]) + 10
    return [s, e]

