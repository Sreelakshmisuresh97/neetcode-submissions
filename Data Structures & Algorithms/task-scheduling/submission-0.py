class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxheap = [-f for f in freq.values()]
        heapq.heapify(maxheap)
        
        maxfreq= abs(heapq.heappop(maxheap))-1
        idle_time = maxfreq*n
        while len(maxheap)>0:
            idle_time -= min(abs(heapq.heappop(maxheap)),maxfreq)
        time = len(tasks)
        if idle_time>0:
            time = idle_time+len(tasks)
        return time
