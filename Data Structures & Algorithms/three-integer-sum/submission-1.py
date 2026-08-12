class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l,r=0,len(nums)-1
        res =[]
        nums.sort()
        for i in range(len(nums)):
            num1 = nums[i]
            if num1 >0:
                break
            if i>0 and num1 == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                sum3 = num1+nums[l]+nums[r]
               
                if sum3 == 0:
                    res.append([num1,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif sum3>0:
                    r-=1
                else:
                    l+=1        
        return res

        