class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        time = 0
        while l<=r:
            m = (l+r)//2
            res = 0
            for i in range(len(piles)):
                res += math.ceil(float(piles[i])/m)
            if(res>h):
                l = m+1
            else:
                time = m
                r= m-1
        return time    

