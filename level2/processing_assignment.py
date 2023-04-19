"""
2023-04-19
https://school.programmers.co.kr/learn/courses/30/lessons/176962
과제 진행하기
"""


def solution(plans):
    answer = []
    plans.sort(key=lambda x: get_minutes(x[1]))

    sub_map = {}
    queue = []
    stack = []

    for plan in plans:
        sub_map[plan[0]] = (get_minutes(plan[1]), int(plan[2]))
        queue.append(plan[0])

    while queue:
        curr_subject = queue.pop(0)
        curr_end_time = sum(sub_map[curr_subject])
        next_start_time = sub_map[queue[0]][0] if queue else float('inf')

        if curr_end_time > next_start_time:
            sub_map[curr_subject] = (0, curr_end_time - next_start_time)
            stack.append(curr_subject)

        elif curr_end_time == next_start_time:
            answer.append(curr_subject)

        else:
            answer.append(curr_subject)

            while stack:
                before_next = stack.pop()
                before_end_time = curr_end_time + sub_map[before_next][1]

                if before_end_time > next_start_time:
                    sub_map[before_next] = (0, before_end_time - next_start_time)
                    stack.append(before_next)
                    break

                elif before_end_time == next_start_time:
                    answer.append(before_next)
                    break

                else:
                    answer.append(before_next)
                    curr_end_time += sub_map[before_next][1]

    return answer


def get_minutes(time):
    time = time.split(':')
    return int(time[0]) * 60 + int(time[1])