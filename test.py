def TwoSum(nums, target):
    newDict = {}

    for i in range(len(nums)): 
        complement = target - nums[i]

        if (complement in newDict.keys()):
            return [i, newDict[complement]]
        else:
            newDict[nums[i]] = i 



nums = [2, 7, 11, 15]
target = 9

print(TwoSum(nums, target))