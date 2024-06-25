class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count=0
        for i in range(len(hours)-1):
            for j in range(i,len(hours)):
                if (hours[i]+hours[j])%24==0 and i<j:
                    count+=1
        return count
