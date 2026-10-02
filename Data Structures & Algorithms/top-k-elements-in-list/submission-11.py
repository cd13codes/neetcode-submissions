from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        ans=[]
        count = Counter(nums)

        for key,value in count.items():
            heapq.heappush(heap,[value,key])
        while len(heap)>k :
            heapq.heappop(heap)
        for hset in heap:
            ans.append(hset[1])
        return ans


        

        
        

        
   
        
