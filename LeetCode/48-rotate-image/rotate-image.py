class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_len = len(matrix)
        
        for row in range(matrix_len):
            for col in range(matrix_len):
                if row <= col:
                    continue
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for row in range(matrix_len):
            for col in range(matrix_len):
                if col >= matrix_len//2:
                    continue
                matrix[row][col], matrix[row][matrix_len-col-1] = matrix[row][matrix_len-col-1], matrix[row][col]