def trap(heights): 
    currL = 0
    currR = len(heights) - 1
    leftMax = heights[currL]
    rightMax = heights[currR]
    water = 0

    while currL != currR: 
        if leftMax <= rightMax:
            currL += 1
            if(heights[currL] > leftMax):
                leftMax = heights[currL]
            
            water += leftMax - heights[currL]
        else: 
            currR -= 1
            if(heights[currR] > rightMax):
                rightMax = heights[currR]
            
            water += rightMax - heights[currR]
    return water


heights = [0,1,0,2,1,0,1,3,2,1,2,1]

print("Total rain trapped is: ", trap(heights))
