# import math
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        if 0 not in nums:
            return 0
        n=max(nums)
        add=n*(n+1)/2
        listadd=sum(nums)
        if add==listadd:
            return int(n+1)
        return int(add-listadd)
