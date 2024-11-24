class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbor_live =  [[0 for col in range(len(board[0]))] for row in range(len(board))]
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 1:
                    for i,j in [[y-1,x-1], [y,x-1], [y+1,x-1], [y-1,x], [y+1,x], [y-1,x+1], [y,x+1], [y+1,x+1]]:
                        if 0<=i<len(board) and 0<=j<len(board[0]):
                            neighbor_live[i][j] += 1

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 0:
                    if neighbor_live[y][x] == 3:
                        board[y][x] = 1
                elif neighbor_live[y][x] < 2:
                    board[y][x] = 0
                elif neighbor_live[y][x] < 4:
                    board[y][x] = 1
                else:
                    board[y][x] = 0