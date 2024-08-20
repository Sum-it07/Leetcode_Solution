class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        i=0
        j=col-1
        result=False
        while i<row and j>=0:
            if matrix[i][j]==target:
                result=True
                break
            if matrix[i][j]<target:
                i+=1
            else:
                j-=1
        return result
