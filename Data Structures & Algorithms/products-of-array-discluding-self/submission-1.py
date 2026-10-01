class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suff=1 
        pref=1 
        prefprod=[1] * len(nums)
        suffprod=[1] * len(nums)
        for i in range(len(nums)): 
            prefprod[i]*=pref
            pref*=nums[i] 
        for i in range(len(nums)-1,-1,-1): 
            suffprod[i]*=(suff*prefprod[i]) 
            suff*=nums[i] 
        return suffprod
        