from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        ans=[]
        count = Counter(nums)

        for key,value in count.items():
            heapq.heappush(heap,[value,key])
            if len(heap)>k :
                heapq.heappop(heap)
        return [num for key,num in heap]


        

        
        

        
   
        
