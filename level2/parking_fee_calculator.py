"""
2023-03-30
https://school.programmers.co.kr/learn/courses/30/lessons/92341
주차 요금 계산
"""

import math

def solution(fees, records):
    answer = []
    num_fee_map = {}
    parked = set()

    for record in records:
        time, number, inout = record.split(" ")
        minutes = to_minutes(time)

        if inout == "IN":
            parked.add(number)
            minutes *= -1
        else:
            parked.remove(number)

        if number in num_fee_map.keys():
            num_fee_map[number] += minutes
        else:
            num_fee_map[number] = minutes

    for number in parked:
        num_fee_map[number] += to_minutes("23:59")

    sorted_keys = sorted(list(num_fee_map.keys()))
    for number in sorted_keys:
        dtime = math.ceil((num_fee_map[number] - fees[0]) / fees[2])
        price = fees[1] + dtime * fees[3] if dtime > 0 else fees[1]
        answer.append(price)

    return answer


def to_minutes(time):
    hours, minutes = time.split(":")
    return int(hours) * 60 + int(minutes)

