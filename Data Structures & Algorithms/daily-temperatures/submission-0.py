class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = []
        
        n = len(temperatures)
        res=[0]*n
        for i in range(n):
            t = temperatures[i]
            while tempStack and t>temperatures[tempStack[-1]]:
                index = tempStack.pop()
                res[index] = i-index
            tempStack.append(i)  
        return res      
            