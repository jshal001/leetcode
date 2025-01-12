def maxProduct(nums):
    maxProduct = nums[0]
    tempProduct = 1

    for val in nums:
        tempProduct *= val
        if tempProduct > maxProduct:
            maxProduct = tempProduct
        elif val > tempProduct:
            maxProduct = val
        

        if tempProduct == 0:
            tempProduct = 1

    return maxProduct
    


nums = [-2,0,-1]

print(maxProduct(nums))