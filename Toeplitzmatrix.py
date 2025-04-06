class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        x=len(matrix)
        acc=None
        for i in range(x):
            if(acc is None):
                acc=matrix[i][i]
            elif(acc!=matrix[i][i]):
                return False
            else:
                acc=matrix[i][i]
        return True    
