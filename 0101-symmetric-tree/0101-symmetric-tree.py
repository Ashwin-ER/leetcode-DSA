# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def dfs(first, second):
            if not first and not second:
                return True 
            if not first or not second:
                return False
            
            return (first.val == second.val and dfs(first.left, second.right) and dfs(first.right, second.left))

        return dfs(root.left, root.right)


        
    
            
        
        """left = self.isSymmetric(root.left)
        rigtht = self.isSymmetric(root.right)"""

"""      if (root.left == root.right) or (root.left == root.right) or (root.right == root.left):
            return True 
        else:
            return False"""

        
        
        