class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            elif stack[-1] + char == "{}" or stack[-1] + char == "[]" or stack[-1] + char == "()":
                stack.pop()
            else:
                stack.append(char)

        if len(stack) == 0:
            return True
        else:
            return False