class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic={}
        for word in strs:
            sortedword = "".join(sorted(word))

            if sortedword in dic:
                dic[sortedword].append(word)
            else:
                dic[sortedword]=[word] 
        return list(dic.values())       