class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        person=1
        right=1
        for i in range(time):
            if right==1 and person<n :
                person+=1
            elif right==0 and person==1:
                right=1
                person+=1
            else:        
                right=0
                person-=1
        return person
