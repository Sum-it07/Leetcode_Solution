class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result=[]
        if target not in nums:
            return [-1,-1]
        else:
            result.append(nums.index(target))
            result.append(len(nums)-1-nums[::-1].index(target))
        return result


