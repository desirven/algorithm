def solution(fees, records):
    import math
    def calc_price(total_time):
        time_diff = total_time - int(fees[0])
        fee = fees[1]
        if time_diff > 0:
            fee += math.ceil(time_diff/fees[2])*fees[3]
        return fee

    current = {}
    total_time = {}
    for record in records:
        time, number, mod = record.split()
        time = int(time.split(':')[0])*60 + int(time.split(':')[1])
        if mod == "IN":
            current[number] = time
            if number not in total_time:
                total_time[number] = 0
        else:
            total_time[number] += time - current[number]
            del current[number]

    for number in current.keys():
        total_time[number] += 23*60+59 - current[number]

    answer = []
    for number in sorted(total_time):
        answer.append(calc_price(total_time[number]))
    return answer