class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        norepeat=set(nums)
        res=0
        count=0
        for i in norepeat:
            if nums.count(i)>count:
                res=i
                count=nums.count(i)
        return res
