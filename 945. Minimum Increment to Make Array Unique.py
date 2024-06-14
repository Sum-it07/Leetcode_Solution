class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # newnums=nums[::-1]
        count=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                temp=nums[i-1]-nums[i]+1
                nums[i]+=temp
                count+=temp
        return count
