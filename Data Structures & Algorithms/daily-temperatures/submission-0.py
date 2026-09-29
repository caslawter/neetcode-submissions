class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                tempIndex = stack.pop()
                result[tempIndex] = index - tempIndex

            stack.append(index)
        return result