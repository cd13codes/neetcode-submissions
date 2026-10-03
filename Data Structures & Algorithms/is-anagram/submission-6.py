class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freqs=[0]*26
        freqt=[0]*26

        for i in s:
            freqs[ord(i)-ord('a')]+=1
        for j in t:
            freqt[ord(j)-ord('a')]+=1
        if(freqs==freqt):
            return True
        else:
            return False
