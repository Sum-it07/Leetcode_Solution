class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max=(2**31)-1
        min=-2**31
        ans=int(dividend/divisor)
        if ans<min:
            return min
        elif ans>max:
            return max
        else:
            return ans
