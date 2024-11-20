def solution(n, words):
    answer = [0,0]
    for i in range(1, len(words)):
        word = words[i]
        if word[0] != words[i-1][-1] or word in words[0:i-1] or len(word) == 1:
            answer = [(i%n)+1, (i//n)+1]
            break
    return answer