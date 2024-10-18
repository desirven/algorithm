def solution(genres, plays):
    total_play = {}
    for idx, (p, g) in enumerate(zip(plays, genres)):
        if g not in total_play:
            total_play[g] = {"total":0, "index":{}}
        total_play[g]["total"] += p
        total_play[g]["index"][idx] = p

    sorted_total_play = dict(sorted(total_play.items(), key=lambda item: item[1]["total"], reverse=True))

    answer = []
    for play_index in sorted_total_play.values():
        sorted_play_index = dict(sorted(play_index["index"].items(), key=lambda item: item[1], reverse=True))
        for idx in list(sorted_play_index.keys())[:2]:
            answer.append(idx)
    return answer