class Solution:

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
