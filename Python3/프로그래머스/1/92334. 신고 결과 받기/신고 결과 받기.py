def solution(id_list, report, k):
    ids_warn = dict.fromkeys(id_list, 0)
    ids_mail = dict.fromkeys(id_list, 0)
    report = list(x.split(' ') for x in set(report))
    black = []
    for r in report:
        if ids_warn[r[1]] > k:
            continue
        ids_warn[r[1]] += 1
        if ids_warn[r[1]] == k:
            black.append(r[1])
    for r in report:
        if r[1] in black:
            ids_mail[r[0]] += 1

    return list(ids_mail.values())