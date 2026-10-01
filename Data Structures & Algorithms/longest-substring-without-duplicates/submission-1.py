class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        mp=1
        seen=set()
        if s=="":
            return 0
        while r<len(s):
            if(s[r] not in seen):
                seen.add(s[r])
                r+=1
                mp=max(mp,r-l)
            else:
                seen.remove(s[l])
                l+=1
            print(seen)
        return mp
            
        
            
            
        