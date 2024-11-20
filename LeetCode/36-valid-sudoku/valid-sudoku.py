from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            cnt = Counter()
            for x in board[i]:
                if x != ".": cnt[x] += 1
            for v in cnt.values():
                if v>1:
                    return False

            cnt = Counter()
            for y in [board[j][i] for j in range(9)]:
                for x in y :
                    if x != ".": cnt[x] += 1
            for v in cnt.values():
                if v>1:
                    return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                cnt = Counter()
                for y in [k[j:j+3] for k in board[i:i+3]]:
                    for x in y:
                        if x != ".": cnt[x] += 1
                for v in cnt.values():
                    if v>1:
                        return False
        return True