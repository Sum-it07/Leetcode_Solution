class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        num=sorted(nums)
        for i in num:
            if i !=num[0] and i!=num[-1]:
                return i
        return -1
