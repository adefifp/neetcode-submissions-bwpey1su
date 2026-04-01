class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            if token == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            if token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            if token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            if token == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(float(a) / b))
        return stack[-1]