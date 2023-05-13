class Solution(object):

    def postorder(self, root):
        res = []
        li = []
        res.append(root)
        if not root:
            return
        while (res):
            temp = res.pop()
            li.append(temp.val)
            for i in temp.children:
                res.append(i)
        return li[::-1]