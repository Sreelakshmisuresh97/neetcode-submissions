class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product,curr_min,curr_max = nums[0],nums[0],nums[0]

        for i in range(1,len(nums)):
            temp = max(nums[i],nums[i]*curr_min,nums[i]*curr_max)
            curr_min = min(nums[i],nums[i]*curr_min,nums[i]*curr_max)

            curr_max = temp
            max_product = max(max_product,temp)
        return max_product    
        