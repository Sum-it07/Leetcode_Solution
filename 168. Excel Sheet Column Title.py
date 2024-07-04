class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        l1=[]
        while(columnNumber>0):
            columnNumber-=1
            div=columnNumber%26
            l1.append(chr(div+ord('A')))
            columnNumber=columnNumber//26
        st="".join(reversed(l1))
        return st
        
