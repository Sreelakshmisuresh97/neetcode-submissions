class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax,curmin =1,1
        res = nums[0]
        for n in nums:
            tmp = n*curMax
            curMax = max(n*curMax,n*curmin,n)
            curmin = min(tmp,n*curmin,n)
            res = max(res,curMax)
        return res