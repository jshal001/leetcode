class Solution: 
    def isValid(self, s): 
        #if size is odd, return false
        if len(s) % 2 == 1: 
            return False
        
        #initalize stack 
        stack = []

        for i in range(len(s)):
            if(s[i] == '(' or s[i] == '{' or s[i] == '['): 
                stack.append(s[i])
            else:
                #if closing character, check if stack isn't empty 
                if(stack):
                    currOpen = stack.pop()
                else: 
                    return False 

                currClosed = s[i]
                if currOpen == '(' and currClosed == ')' or currOpen == '[' and currClosed == ']' or currOpen == '{' and currClosed == '}': 
                    continue
                else: 
                    return False
        #if number of closing characters = number of open characters
        if not stack: 
            return True
        
        return False

# Time Complexity: O(n)
# Space Complexity: O(n)