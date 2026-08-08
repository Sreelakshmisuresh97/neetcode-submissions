class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adjList =[[] for i in range(numCourses)]
        for dest,src in prerequisites:
            indegree[dest]+=1
            adjList[src].append(dest)
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        finish=0
        while q:
            crs= q.popleft()
            finish+=1
            for i in adjList[crs]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        return finish==numCourses

