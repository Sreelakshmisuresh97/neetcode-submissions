class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2:
            return False
        target = total//2
        dp = set()
        dp.add(0)
        for i in range(len(nums) - 1, -1, -1):
            temp = set()
            for s in dp:
                if s+nums[i] == target:
                    return True
                temp.add(s+nums[i])
                temp.add(s)
            dp = temp
        return False
        
        