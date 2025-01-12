def majorityElement(nums): 
    count = 0
    candidate = 2

    for num in nums:
        if(count == 0): 
            candidate = num
        
        if num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate



nums = [3,2,3]

print(majorityElement(nums))