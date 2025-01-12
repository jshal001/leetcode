def lengthOfLongestSubstring(s):
    l = 0

    longestLength = 0

    window = set()

    for r in range(len(s)):
        while s[r] in window: 
            window.remove(s[l])
            l += 1
    
        window.add(s[r])
        longestLength = max(longestLength, r - l + 1)
    print(window)
    return longestLength

example = "abacsdfalskdjfasldkjf"

print(lengthOfLongestSubstring(example))