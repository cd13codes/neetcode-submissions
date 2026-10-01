class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxa=[]
        for i in range (len(heights)):
           j=i+1
           while j<len(heights):
             minheight=min(heights[j],heights[i])
             area=(j-i)*minheight
             maxa.append(area)
             j+=1
        return max(maxa)



        