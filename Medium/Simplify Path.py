class Solution:

    def simplifyPath(self, path: str) -> str:
        cadenas = path.split('/')
        arr = []
        for s in cadenas:
            if s != '.' and s != '..' and s:
                arr.append(s)
            elif s == "..":
                if arr:
                    arr.pop()

        return '/' + '/'.join(arr)