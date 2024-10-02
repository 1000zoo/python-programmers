"""
2024-10-02
https://school.programmers.co.kr/learn/courses/30/lessons/150368
이모티콘 할인행사
"""

def solution(users, emoticons):
    answer = [0, 0]
    length = len(emoticons)
    discount_rate = [10] * length

    while discount_rate[-1] <= 40:
        total_user = 0
        total_price = 0

        for user in users:
            temp = 0
            for i in range(length):
                if user[0] <= discount_rate[i]:
                    temp += emoticons[i] * (1 - discount_rate[i] / 100)

            if user[1] <= temp:
                total_user += 1
            else:
                total_price += temp

        if answer[0] < total_user:
            answer[0] = total_user
            answer[1] = total_price
        elif answer[0] == total_user:
            answer[1] = max(answer[1], total_price)

        discount_rate = getNext(discount_rate)

    return answer


def getNext(dr):
    dr[0] += 10
    for i in range(len(dr) - 1):
        if dr[i] > 40:
            dr[i] = 10
            dr[i + 1] += 10

    return dr