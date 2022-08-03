class Solution:
    def isPalindrome(self, s): 
        """
        :type s: str
        :rtype: bool
        """

        #remove all non alpha num characters 
        s = ''.join( filter(str.isalnum, s)).lower()

        left = 0
        right = len(s) - 1

        while(right > left):
            if s[right] != s[left]: 
                return False

            right -= 1
            left += 1
        return True

    
solution = Solution()
print(solution.isPalindrome('gg'))

#time complexity: O(n)
#space complexity: O(1)