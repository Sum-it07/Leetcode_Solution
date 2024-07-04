class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        count=0
        if len(columnTitle)==1:
            return ord(columnTitle)-64
        for i in range(len(columnTitle)):
            count=count*26+(ord(columnTitle[i])-ord('A')+1)
        return count
