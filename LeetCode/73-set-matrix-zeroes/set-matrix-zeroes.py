class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        modify_element = set()
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    for y2 in range(len(matrix)):
                        modify_element.add((y2,x))
                    for x2 in range(len(matrix[0])):
                        modify_element.add((y,x2))
        for y, x in modify_element:
            matrix[y][x] = 0