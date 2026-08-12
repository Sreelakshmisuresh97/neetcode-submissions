class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneheap = [-s for s in stones]
        heapq.heapify(stoneheap)
        while len(stoneheap)>1:
            n1 = heapq.heappop(stoneheap)
            n2 = heapq.heappop(stoneheap)
            if n2>n1:
                heapq.heappush(stoneheap,n1-n2)
        stoneheap.append(0)
        return stoneheap[0]*-1       