# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []
        if root:
            q.append(root)
        while q:
            n = len(q)
            
            for i in range(n):
                num = q.popleft()
                if num.left:
                    q.append(num.left)
                if num.right:
                    q.append(num.right)    
                if i == n-1:
                    res.append(num.val)
        return res               
            
