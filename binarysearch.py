class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0 
        r = len(nums) - 1
        mid = (l + r ) // 2

        while (l <= r):
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
                mid = (l + r ) // 2
            else:
                l = mid + 1
                mid = (l + r ) // 2
        return -1

# Time Complexity = O(logn)
# Space Complexity = O(1)


