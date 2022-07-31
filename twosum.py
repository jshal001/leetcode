class Solution: 
    def twoSum(self, nums, target): 
        keyDict = {}

        for i in range(len(nums)): 
            complement = target - nums[i]


            if complement in keyDict.keys():
                return [i, keyDict[complement]]
            keyDict[nums[i]] = i

#Time Complexity: O(n)

#Space Complexity: O(n)