class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        arr=[]
        for i in nums:
            counts[i]=1+counts.get(i,0) 
        s=sorted(counts.items(), key = lambda x:-x[1]) 
        a=dict(s)
        l=list(a.keys())
        
        return l[:k]
        


    
        
            
        