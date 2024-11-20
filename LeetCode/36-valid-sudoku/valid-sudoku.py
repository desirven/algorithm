class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_cnt = [set() for _ in range(9)]
        col_cnt = [set() for _ in range(9)]
        box_cnt = [set() for _ in range(9)]


        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                val = board[row][col]
                box_idx = (row//3)*3+(col//3)
                if val in row_cnt[row] or val in col_cnt[col] or val in box_cnt[box_idx]:
                    return False
                row_cnt[row].add(val)
                col_cnt[col].add(val)
                box_cnt[box_idx].add(val)

        return True