class MedianFinder:

    def __init__(self):
        self.largeheap = []
        self.smallheap = []


    def addNum(self, num: int) -> None:
        if self.largeheap and num>self.largeheap[0]:
            heapq.heappush(self.largeheap,num)
        else:
            heapq.heappush(self.smallheap,num*-1)
        if len(self.smallheap) > len(self.largeheap)+1:
            val = -1 * heapq.heappop(self.smallheap)
            heapq.heappush(self.largeheap,val)
        if len(self.largeheap) > len(self.smallheap) + 1:
            val = -1 * heapq.heappop(self.largeheap)
            heapq.heappush(self.smallheap,val)             

    def findMedian(self) -> float:
        if len(self.smallheap) > len(self.largeheap):
            return -1*self.smallheap[0]
        if len(self.largeheap) > len(self.smallheap):
            return self.largeheap[0]
        else:
            return (-1*self.smallheap[0]+self.largeheap[0])/2    
        
        