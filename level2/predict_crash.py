"""
2024-09-11
https://school.programmers.co.kr/learn/courses/30/lessons/340211
충돌위험 찾기
"""

def solution(points, routes):
    answer = 0
    all_routes = []
    max_index = 0
    for route in routes:
        route_points = []
        for i in range(len(route) - 1):
            p1 = points[route[i] - 1]
            p2 = points[route[i + 1] - 1]

            route_points.extend(getRoutePoints(p1, p2))
        route_points.append(tuple(points[route[-1] - 1]))
        all_routes.append(route_points)
        max_index = max(max_index, len(route_points))

    for point_index in range(max_index):
        crash_map = {}
        for route in all_routes:
            if len(route) <= point_index:
                continue
            point = route[point_index]
            crash_map[point] = True if point in crash_map.keys() else False
        for _, crash in crash_map.items():
            if crash:
                answer += 1

    return answer


def getRoutePoints(p1, p2):
    r1, c1 = p1
    r2, c2 = p2
    route_points = []

    direct_r = 1 if r1 < r2 else -1

    for r in range(r1, r2 + direct_r, direct_r):
        route_points.append((r, c1))

    direct_c = 1 if c1 < c2 else -1
    for c in range(c1 + direct_c, c2 + direct_c, direct_c):
        route_points.append((r2, c))
    route_points.pop()
    return route_points


