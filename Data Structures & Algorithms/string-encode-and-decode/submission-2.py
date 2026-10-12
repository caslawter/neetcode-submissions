class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""

        if len(strs) == 0:
            return ""
        
        for string in strs:
            length = len(string)
            encode += f"{length}#{string}"
        return encode

    def decode(self, s: str) -> List[str]:
        ans = []
        tempCount = ""
        count = 0
        string = ""

        if s == "":
            return []
        
        for char in s:

            if char.isdigit() and count == 0:
                tempCount += char
                continue
            elif char == "#" and count == 0:
                count = int(tempCount)
                tempCount = ""
                if count == 0:
                    ans.append(string)
                continue

            if count >= 0:
                string += char
                count -= 1

            if count == 0:
                ans.append(string)
                string = ""

        return ans