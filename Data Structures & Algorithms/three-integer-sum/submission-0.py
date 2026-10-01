class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=0
        lst=[]

        for i in range (len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates at i
                continue
           
            target=nums[i]
            j=i+1
            k=(len(nums))-1
            while(j<k):
                if(-target==(nums[j]+nums[k])):
                    lst.append([target,nums[j],nums[k]])
                    j+=1
                    k-=1
                    if nums[j] == nums[j - 1]:
                        j += 1
                    # Skip duplicate values at k
                    if  nums[k] == nums[k + 1]:
                        k -= 1
                elif(-target<(nums[j]+nums[k])):
                    k=k-1
                else:
                    j=j+1
        
        return(lst)



        