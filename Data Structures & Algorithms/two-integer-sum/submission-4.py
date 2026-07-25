class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(len(nums)):
            n = target-nums[i]
            if n in numDict:
                return[numDict[n],i]
            numDict[nums[i]] = i

