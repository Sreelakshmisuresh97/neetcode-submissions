# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValidBSTUtil(node,mini,maxi):
            if node is None:
                return True 
            if not mini<node.val<maxi:
                return False
            return  isValidBSTUtil(node.left,mini,node.val) and isValidBSTUtil(node.right,node.val,maxi)
        return isValidBSTUtil(root,float('-inf'),float("inf"))     

