class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for ops in operations:
            if ops == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                total = num1 + num2
                stack.append(num2)
                stack.append(num1)
                stack.append(total)
            elif ops == "C":
                stack.pop()
            elif ops == "D":
                num1 = stack[-1]
                total = num1 * 2
                stack.append(total)
            else:
                stack.append(int(ops))
        ans = 0

        for i in stack:
            ans += i
        return ans
            
            