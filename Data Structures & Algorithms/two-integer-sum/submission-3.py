class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_dict = {}
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in target_dict:
                return [target_dict[num2],i]
            target_dict[nums[i]] = i    