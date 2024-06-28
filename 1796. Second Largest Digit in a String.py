class Solution:
    def secondHighest(self, s: str) -> int:
        digit=['0','1','2','3','4','5','6','7','8','9']
        # s.split()
        new=[]
        for i in range(len(digit)):
            if digit[i] in s and digit[i] not in new:
                new.append(int(digit[i]))
        
        if len(new)<=1:
            return -1
        else:
            return new[-2]
