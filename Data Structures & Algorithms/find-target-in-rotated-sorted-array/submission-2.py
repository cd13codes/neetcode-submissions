class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while(l<r):
            mid=(l+r)//2
            if(nums[mid]>nums[r]):
                l=mid+1
            else:
                r=mid
        br=l
        arr1=nums[:br]
        arr2=nums[br:]
        
        def binse(arr,target):
            l,r=0,len(arr)-1
            while(l<=r):
                mid=(l+r)//2
                if(arr[mid]==target):
                    return mid
                elif(arr[mid]<target):
                    l=mid+1
                else:
                    r=mid-1
            return -1

        if(binse(arr1,target)!=-1):
            return binse(arr1,target)
        elif(binse(arr2,target)!=-1):
            return binse(arr2,target)+br
        else:
            return -1
        

    

