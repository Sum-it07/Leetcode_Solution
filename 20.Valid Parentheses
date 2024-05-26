class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if len(stack)==0 or mapping[char] != stack.pop():
                    return False
        
        if len(stack)==0:
            return True
        else:
            return False
