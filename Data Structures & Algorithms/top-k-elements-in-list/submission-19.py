from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count=Counter(nums)
        dic={}
        ans=[]
        
        for i in range(len(nums)+1):

            dic[i]=[]

        for key,value in count.items():

            dic[value].append(key)

        for value in dic.values():

            ans.extend(value)
        
        



        return ans[(len(ans)-k):]
        
        



        



















        