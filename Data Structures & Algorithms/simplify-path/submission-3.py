class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        word = ""
        index = 0

        while index <= len(path) - 1:
            if path[index] == "/":
                if word == "..":
                    if len(stack) != 0:
                        stack.pop()
                elif word != "" and word != ".":
                    stack.append(word)
                word = ""
            else:
                word += path[index]
            index += 1
        
        if len(word) > 0 and word != ".." and word != ".":
            stack.append(word)
        elif word == "..":
            if len(stack) > 0:
                stack.pop()
        path = "/"

        for index, word in enumerate(stack):
            if index >= len(stack) - 1:
                path += f"{word}"
            else:
                path += f"{word}/"
        return path

            
                