# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?
import heapq
def heapSelect(nums, k):
    minHeap = nums[:k]
    heapq.heapify(minHeap)

    for val in nums[k:]: 
        if (val > minHeap[0]):
            heapq.heapreplace(minHeap, val)
    
    return minHeap[0]
    

    



def quickSelect(left, right, nums):
    #assign pivot 
    pivot, fill = nums[right], left

    for i in range(left, right): 
        if pivot >= nums[i]: 
            nums[fill], nums[i] = nums[i], nums[fill]

            fill += 1
    
    nums[fill], nums[right] = nums[right], nums[fill]

    return fill


def findKthLargest(nums, k):
    #reassign k to be the position in the array 
    k = len(nums) - k
    
    left, right = 0, len(nums) - 1

    while left < right: 
        pivot = quickSelect(left, right, nums)

        if pivot > k: 
            right = pivot - 1

        elif pivot < k: 
            left = pivot + 1

        else: 
            break

    return nums[k]
    
nums = [3,2,1,5,6,4]
k = 6

print(heapSelect(nums, k))