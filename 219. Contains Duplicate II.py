class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict1={}
        ans=False
        for i in range(len(nums)):
            if nums[i] in dict1 and i-dict1[nums[i]]<=k:
                ans=True
            dict1[nums[i]]=i
        return ans

        
