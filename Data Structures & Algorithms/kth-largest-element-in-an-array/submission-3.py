class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = nums
        heapq.heapify(maxHeap)
        n = len(nums)-k
        i=0
        while i<n:
            heapq.heappop(maxHeap)
            i+=1
        return heapq.heappop(maxHeap)   

        