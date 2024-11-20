from collections import deque

def is_one_difference(word1, word2):
    diff = 0
    for char1, char2 in zip(word1, word2):
        if char1 != char2:
            diff += 1
    if diff == 1:
        return True
    return False

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = []
    que = deque()
    que.append((begin, 0))
    
    while que:
        current_word, depth = que.popleft()
        if current_word == target:
            return depth
        
        for next_word in words:
            if is_one_difference(current_word, next_word) and next_word not in visited:
                visited.append(next_word)
                que.append((next_word, depth+1))