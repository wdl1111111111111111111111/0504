def maxArea(height: list[int]) -> int:
    i,j,res=0,len(height)-1,0
    while i<j:
        if height[i]<height[j]:
            res=max(res,(j-i)*(height[i]))
            i+=1
        else:
            res=max(res,(j-i)*(height[j]))
            j-=1
    return res
