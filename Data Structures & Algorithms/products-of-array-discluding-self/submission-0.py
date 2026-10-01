class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        j=1
        arr=[]
        for i in range (len(nums)):
            if nums[i]==0:
                continue
            else:
                j=j*nums[i]
        for k in range (len(nums)):
            if nums.count(0)>1:
                arr=[0]*len(nums)
            elif(nums.count(0)==1):
                arr=[0]*len(nums)
                o=nums.index(0)
                arr[o]=j
            else:
                arr.append(int(j/nums[k]))
        return arr

        
            

             
        