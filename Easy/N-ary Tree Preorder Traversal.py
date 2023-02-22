class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        arr = []

        def order(root):
            if root is None:
                return None
            arr.append(root.val)
            for i in root.children:
                order(i)

        order(root)
        return arr
