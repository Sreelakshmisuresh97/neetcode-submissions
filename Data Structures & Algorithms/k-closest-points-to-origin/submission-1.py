class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            dist = (x**2 + y**2)
            heapq.heappush(minHeap,[dist,x,y])
        i =0
        res=[]
        while i<k:
            dist,x,y = heapq.heappop(minHeap)
            res.append([x,y])
            i+=1
        return res    

        