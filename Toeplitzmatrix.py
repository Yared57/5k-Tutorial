class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        
        for i in range(cols):
            Acc = matrix[0][i]
            r, c = 0, i
            while r < rows and c < cols:
                if matrix[r][c] != Acc:
                    return False
                r += 1
                c += 1

        for i in range(1, rows):
            Acc = matrix[i][0]
            r, c = i, 0
            while r < rows and c < cols:
                if matrix[r][c] != Acc:
                    return False
                r += 1
                c += 1

        return True
