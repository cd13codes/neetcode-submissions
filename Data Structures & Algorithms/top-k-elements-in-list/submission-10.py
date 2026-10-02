from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        count = Counter(nums)

        buckets=[[]for _  in range(len(nums)+1)]

        # print(buckets)
        # print(count)

        for num,frequency in count.items():
            buckets[frequency].append(num)
        
        #print(buckets)

        for index in buckets:
            for char in index:
                ans.append(char)

        return ans[len(ans)-k:]
   
        
