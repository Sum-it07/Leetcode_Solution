class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new=set(nums)
        if len(new)==len(nums):
            return False
        else:
            return True
