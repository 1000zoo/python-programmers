"""
2023-03-27
https://school.programmers.co.kr/learn/courses/30/lessons/150370
개인정보 수집 유효기간
"""

def solution(today, terms, privacies):
    answer = []
    terms_json = {}
    today = trans_date(today)

    for term in terms:
        t, m = term.split(' ')
        terms_json[t] = int(m) * 28

    for i, priv in enumerate(privacies):
        date, t = priv.split(' ')
        delta_month = int(terms_json[t])
        _date = trans_date(date)
        if _date + delta_month <= today:
            answer.append(i + 1)

    return answer

def trans_date(date):
    ty, tm, td = [int(n) for n in date.split('.')]
    return (ty - 2000) * 12 * 28 + tm * 28 + td

