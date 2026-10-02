class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freqs = [0]*26
        freqt = [0]*26

        for char in s :
            freqs[ord(char)-ord('a')]+=1
        for char in t :
            freqt[ord(char)-ord('a')]+=1
        if (freqs == freqt):
            return True
        else:
            return False
        
        