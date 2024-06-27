class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dest=''
        start=[]
        end=[]
        for i in range(len(paths)):
            start.append(paths[i][0])
            end.append(paths[i][1])
        for i in end:
            if i not in start:
                dest=i
        return dest
