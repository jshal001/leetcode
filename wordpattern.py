# Input: pattern = "abba", s = "dog cat cat dog"

# Output: true

def wordPattern(pattern: str, s: str) -> bool:
    patternMap = {}
    sMap = {}
    s = s.split()

    if len(s) != len(pattern):
        return False
    for i in range(len(pattern)): 
        if (pattern[i] in patternMap.keys()): 
            if patternMap[pattern[i]] != s[i]:
                return False
        if s[i] in sMap.keys():
            if sMap[s[i]] != pattern[i]:
                return False
        else: 
            patternMap[pattern[i]] =  s[i]
            sMap[s[i]] = pattern[i]
    
    return True

pattern,s = "abc", "dog cat dog"

print(wordPattern(pattern, s))
