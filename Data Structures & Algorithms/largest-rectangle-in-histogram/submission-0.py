class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i,n in enumerate(heights):
            s = i

            while stack and stack[-1][1]>n:
                idx,h = stack.pop()
                max_area = max(max_area,(i-idx)*h)
                s= idx
            stack.append([s,n])
        while stack:
            i = stack[-1][0]
            h = stack[-1][1]
            max_area = max(max_area,(len(heights)-i)*h)
            stack.pop()
        return max_area        