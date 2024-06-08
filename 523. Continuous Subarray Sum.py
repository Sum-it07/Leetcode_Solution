class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dict={0:-1}
        rem=0
        for i in range(len(nums)):
            rem+=nums[i]
            rem%=k
            if rem in dict:
                if i-dict[rem]>1:
                    return True
            else:
                dict[rem]=i 
        return False

