from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count=Counter(nums)
        heap=[]
        hset=[]

        for key,value in count.items():

            heapq.heappush(heap,[value,key])

            while len(heap)>k:
                heapq.heappop(heap)
        
        for item in heap:
            hset.append(item[1])
        return hset



        