class Solution:
    def addDigits(self, num: int) -> int:
        temp=num
        while(temp>=10):
            sum=0
            while(num>0):
                temp=num%10
                sum+=temp
                num=(num//10)
            num=sum
            temp=num

        return num
