class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        newlist=[]
        xor=0
        for i in range(len(nums)):
            if nums[i] in newlist:
                xor^=nums[i]
            else:
                newlist.append(nums[i])
        return xor
