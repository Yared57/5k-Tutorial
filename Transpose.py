class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        Mat = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                Mat[i][j]=matrix[j][i]
        return Mat   
