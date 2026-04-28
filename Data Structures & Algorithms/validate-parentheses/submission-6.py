class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}  # opening -> closing
        
        for char in s:
            if char in pairs:  # if it's an opening bracket
                stack.append(char)
            elif char in ')}]':  # if it's a closing bracket
                if not stack:  # nothing to match with
                    return False
                if pairs[stack.pop()] != char:  # last open doesn't match
                    return False
        
        return len(stack) == 0  # True if all opened brackets were closed