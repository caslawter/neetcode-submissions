class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        stack2 = []
        ban = [" ", "?", ".",",", "'",":","!"]
        for i in s:
            if i not in ban:
                stack.append(i.lower())
                stack2.append(i.lower())
        stack2.reverse()
        print(stack)
        print(stack2)
        if stack == stack2:
            return True
        else:
            return False