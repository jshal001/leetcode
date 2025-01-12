def productExceptSelf(nums):
#     #take the product all values except self at each index
#     #e.g. [1,2,3,4] => [24,12,8,6]

    #traverse left to right 
    left = 1
    tempNums = [1] * len(nums)

    for i in range(len(nums) - 1):
        left*= nums[i]
        tempNums[i+1] = left

    #right traversal
    right = 1
    for i in range(len(nums) - 1, 0, -1):
        right *= nums[i]
        tempNums[i - 1] = right * tempNums[i - 1]

    return tempNums






nums = [-1,1,0,-3,3]

print(productExceptSelf(nums))