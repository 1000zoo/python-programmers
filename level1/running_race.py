"""
2023-04-11
https://school.programmers.co.kr/learn/courses/30/lessons/178871
달리기 경주
"""

def solution(players, callings):
    ranks_map = {}

    for i, player in enumerate(players):
        ranks_map[player] = i

    for calling in callings:
        rank_index = ranks_map[calling]

        front_player = players[rank_index - 1]
        called_player = players[rank_index]

        players[rank_index] = front_player
        players[rank_index - 1] = called_player

        ranks_map[front_player] = rank_index
        ranks_map[called_player] = rank_index - 1

    return players