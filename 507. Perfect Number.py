class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<3:
            return False
        sum=1
        for i in range(2,int(num**(1/2))+1):
            if num%i==0:
                sum+=i
                if i!=num//i:
                    sum+=(num//i)
        if sum==num:
            return True
        else:
            return False
            
