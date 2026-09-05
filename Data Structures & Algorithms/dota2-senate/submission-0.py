class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D,R = deque(),deque()
        n=len(senate)

        for i,c in enumerate(senate):
            if c=='R':
                R.append(i)
            else:
                D.append(i)
        
        while D and R:
            d=D.popleft()
            r = R.popleft()

            if d<r:
                D.append(d+n)
            else:
                R.append(r+n)
        return "Radiant" if R else "Dire"