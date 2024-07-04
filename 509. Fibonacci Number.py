class Solution:
    def fib(self, n: int) -> int:
        l1=[0,1]
        for i in range(2,n+1):
            l1.append(l1[i-1]+l1[i-2])
        return l1[n]
