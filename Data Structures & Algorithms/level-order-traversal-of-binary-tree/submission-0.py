# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        res = []
        if root is None:
            return []
        q.append(root)
        while q:
            n = len(q)
            temp = []
            for i in range(n):
                num = q.popleft()
                temp.append(num.val)
                if num.left:
                    q.append(num.left)
                if num.right:
                    q.append(num.right)    
            res.append(temp)
        return res    
