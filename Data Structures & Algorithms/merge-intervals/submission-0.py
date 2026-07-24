class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        output=[intervals[0]]
        for start,end in intervals:
            last = output[-1][1]
            if last>=start:
                output[-1][1]=max(last,end)
            else:
                output.append([start,end])
        return output