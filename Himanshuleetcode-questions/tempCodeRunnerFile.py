class Solution:
    def maxArea(height):
        left=0
        right=len(height)-1
        g_area=0
        while left<right:
            area=min(height[left],height[right])*(right-left)
            g_area=max(g_area,area)
            if(height[left]<height[right]):
                left+=1
            elif(height[right]<height[left]):
                right-=1
            else:
                left+=1
                right-=1
        return g_area
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))