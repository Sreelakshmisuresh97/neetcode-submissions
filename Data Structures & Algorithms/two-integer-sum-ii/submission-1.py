class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l<r:
            num1 = numbers[l]
            num2 = numbers[r]
            sum1 = num1+num2
            if(sum1 == target):
                return (l+1,r+1)
            elif sum1>target:
                r-=1
            else:
                l+=1      