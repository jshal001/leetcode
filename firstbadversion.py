# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
import math
class Solution(object):
    def firstBadVersion(self, n):
        l, r = 1, n
        result = 0
        while l <= r:
            m = (l+r) // 2
            if isBadVersion(m):
                result = m
                r = m-1
            else:
                l = m+1
        return result

#Time Complexity: O(Log(n))
#Space Complexity: O(1)