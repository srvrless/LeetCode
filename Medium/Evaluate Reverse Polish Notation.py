class Solution:
    def evalRPN(self, expression: List[str]) -> int:
        stack = []

        for ele in expression:

            if ele not in '/*+-':
                stack.append(int(ele))
            else:
                right = stack.pop()
                left = stack.pop()

            if ele == '+':
                stack.append(left + right)

            elif ele == '-':
                stack.append(left - right)

            elif ele == '*':
                stack.append(left * right)

            elif ele == '/':
                stack.append(int(left / right))

        return stack.pop()
