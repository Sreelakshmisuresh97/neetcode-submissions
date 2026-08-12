class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = [-n for n in nums]
        heapq.heapify(minheap)
        for i in range(k-1):
            heapq.heappop(minheap)
        return minheap[0]*-1