class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2!=0:
            return False
        dp={0}
        for i in range(len(nums)):
            temp =set(dp)
            for s in dp:
                temp.add(s+nums[i])
            dp = temp
            if total//2 in dp:
                return True
        return False

