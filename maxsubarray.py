class Solution: 
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tempSum = 0
        maxSum = nums[0]

        for i in range(len(nums)): 
            tempSum += nums[i]
            if(tempSum > maxSum):
                maxSum = tempSum
            
            if(tempSum < 0):
                tempSum = 0
            
        return maxSum

solution = Solution()

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(solution.maxSubArray(nums))

#Time Complexity = O(n)
#Space Complexity = O(1)


