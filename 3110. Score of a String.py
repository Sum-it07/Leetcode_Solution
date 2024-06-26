class Solution:
    def scoreOfString(self, s: str) -> int:
        list1=[]
        for i in range(1,len(s)):
            diff=abs(ord(s[i])-ord(s[i-1]))
            list1.append(diff)
        count=sum(list1)
        return count
