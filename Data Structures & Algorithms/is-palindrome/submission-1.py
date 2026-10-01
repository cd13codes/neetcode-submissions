class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=[]
        for i in range(len(s)):
            if (s[i].isalnum()):
                a.append(s[i].lower())

        for i in range(len(a)):
            if a[i]!=a[len(a)-i-1]:
                return False
                
        return True


        
            


        

        