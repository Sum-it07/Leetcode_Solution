class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        value=False
        for i in range(n):
            if pow(2,i)==n:
                value=True
            if pow(2,i)>n:
                break
        return value
