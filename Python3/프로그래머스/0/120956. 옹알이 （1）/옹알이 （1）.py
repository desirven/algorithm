def solution(babbling):
    answer = 0

    for n in range(len(babbling)):
        word = babbling[n]
        i = 0
        tmp = ""
        while True:
            if i == len(word):
                answer += 1
                break
            elif (word[i: i + 2] in ["ye", "ma"]) and not (word[i: i + 2] == tmp):
                tmp = word[i:i + 2]
                i += 2
            elif (word[i: i + 3] in ["aya", "woo"]) and not (word[i: i + 3] == tmp):
                tmp = word[i:i + 3]
                i += 3
            else:
                break

    return answer 