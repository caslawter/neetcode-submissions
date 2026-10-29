class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if len(stack) == 0:
                stack.append(asteroid)
            elif asteroid < 0 and stack[-1] > 0:
                while True:
                    if asteroid < 0 and stack[-1] < 0:
                        stack.append(asteroid)
                        break
                    if abs(asteroid) == abs(stack[-1]):
                        stack.pop()
                        break
                    elif abs(asteroid) > abs(stack[-1]):
                        stack.pop()
                        if len(stack) == 0:
                            stack.append(asteroid)
                            break
                    else:
                        break
            else:
                stack.append(asteroid)
        return stack