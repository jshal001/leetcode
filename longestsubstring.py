from collections import deque

def lengthOfLongestSubstring(s):
    l = 0
    window = deque()

    longest_substr = ""
    windowSize = 0

    while l < len(s):
        while s[l] in window:
            window.popleft()
        if len(window) > windowSize:
            windowSize = len(window)
            longest_substr = window
        
        l += 1
        
        return 

    

    