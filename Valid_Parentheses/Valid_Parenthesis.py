class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}
        
        for c in s:
            if c in closeToOpen: # a closing bracket
                if stack and stack[-1] == closeToOpen[c]: # must both be closing
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) # add to stack if its a open 

        return True if not stack else False # stack must be empty for true