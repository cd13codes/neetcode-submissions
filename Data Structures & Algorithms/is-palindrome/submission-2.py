class Solution:
    def isPalindrome(self, s: str) -> bool:

        y=[]

        for x in s :
            if x.isalnum() :
                y.append(x.upper())
        print(y)

        

        for i in range(len(y)//2):

            first=y[i]
            last=y[-(1+i)]

            print(first)
            print(last)

            if first != last :
                return False
            
        return True
        