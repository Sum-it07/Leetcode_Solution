class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums==[]:
            return 1
        nums=sorted(nums)
        if nums[0]<0:
            for i in range(len(nums)):
                if nums[i]>=1:
                    nums[:]=nums[i:]
                    break
        ans=1
        for i in nums:
            if i==ans:
                ans+=1
        return ans
