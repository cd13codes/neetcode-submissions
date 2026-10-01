class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ctp={")":"(","}":"{","]":"["}

        for c in s:
            if c in ctp:
                if not stack or stack.pop()!=ctp[c]:
                    return False
            else:
                    stack.append(c)
            
        return not stack
               

        