class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """ 
        if root is None and subRoot is None:
            return True
        if subRoot is None:
            return True
        if root is None and subRoot is not None:
            return False
        return self.isSame(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def isSame(self,root,subRoot):
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        return root.val == subRoot.val and self.isSame(root.left,subRoot.left) and self.isSame(root.right,subRoot.right)