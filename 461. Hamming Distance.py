class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        pos=x^y
        count=0
        while pos:
            count+=pos&1
            pos=pos>>1
        return count
