class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res=['']*numRows
        down=False
        rows=0
        if len(s)<=numRows or numRows==1:
            return s
        for char in s:
            res[rows]+=char
            if rows==0 or rows==numRows-1:
                down=not down
            if down==True:
                rows+=1
            else:
                rows-=1
        return "".join(res)
