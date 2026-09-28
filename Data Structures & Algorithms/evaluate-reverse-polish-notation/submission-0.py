class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["*", "+", "-", "/"]

        for char in tokens:
            if char not in operations:
                stack.append(int(char))
            else:
                value1 = stack.pop()
                value2 = stack.pop()
                value = 0
                if char == "*":
                    value = value2 * value1
                elif char == "+":
                    value = value2 + value1
                elif char == "-":
                    value = value2 - value1
                elif char == "/":
                    value = value2 / value1

                stack.append(int(value))
        return int(stack[0])