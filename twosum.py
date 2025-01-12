
def twoSum(nums, target): 
    keyDict = {}

    for i in range(len(nums)): 
        complement = target - nums[i]


        if complement in keyDict.keys():
            return [keyDict[complement], i]
        keyDict[nums[i]] = i

nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))


