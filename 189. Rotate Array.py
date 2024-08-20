class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:]=nums[::-1]
        nums[:]=nums[k:]+nums[:k]
        nums[:]=nums[::-1]
