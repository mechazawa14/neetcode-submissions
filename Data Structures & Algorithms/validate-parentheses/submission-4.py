class Solution:
    def isValid(self, s: str) -> bool:
        valid_pair = {'[': ']' , '{': '}' , '(': ')'}

        stack = []
        for i in s :
            if i in valid_pair :
                stack.append(i)
            elif i in ']})':
                if len(stack) == 0 :
                    return False 
                else :
                    if valid_pair[stack.pop()] !=  i :
                        return False 
        if len(stack)== 0:
            return True 
        return False 
