class Solution:
    def isValid(self, s: str) -> bool:

        d = {"(":")","{":"}","[":"]"}
        stack=[]

        for bracket in s :
            
            if bracket in d :

                stack.append(bracket)
            
            else:

                if (stack == [] or d[stack.pop()]!=bracket):

                    return False
                
        return True if stack == [] else False
            



        