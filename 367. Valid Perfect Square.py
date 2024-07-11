class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a=int(num**0.5)
        b=int(a**2)
        if num==b:
            return True
        else:
            return False
