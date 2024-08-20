class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        result=False
        for i in range(4):
            if mat==target:
                result=True
                break
            for i in range(len(mat)):
                for j in range(i,len(mat)):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            for i in range(len(mat)):
                mat[i].reverse()

        return result

        
