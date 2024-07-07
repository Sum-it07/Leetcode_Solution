class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res=numBottles

        while numBottles>=numExchange:
            temp=numBottles//numExchange
            rem=numBottles%numExchange
            res+=temp
            numBottles=temp+rem
        return res
