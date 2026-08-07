class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        def backtrack(i,cur):
            if i>=len(nums):
                res.add(tuple(cur.copy()))
                return
            cur.append(nums[i])
            backtrack(i+1,cur)
            cur.pop()
            backtrack(i+1,cur)

        backtrack(0,[])
        return [list(s) for s in res]
            