class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        new=[]
        for i in range(len(matrix)):
            temp=[]
            for j in range(1,len(matrix)+1):
                temp.append(matrix[-j][i])
            new.append(temp)
        matrix[:]=new
