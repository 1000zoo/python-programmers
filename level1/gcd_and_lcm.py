"""
2023-07-18
https://school.programmers.co.kr/learn/courses/30/lessons/12940?language=python3
최대공약수와 최소공배수
"""

def solution(n, m):
    gcd = lambda n, m: gcd(m, n % m) if m != 0 else n
    return [gcd(n, m), (n * m) // gcd(n, m)]