
def romanToInt(s: str) -> int:

    romanDict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    i = 0
    while i < len(s):
        if s[i] in ("I", "X", "C") and i + 1 < len(s):
            if (s[i] == "I" and s[i + 1] in ("V", "X")) or \
            (s[i] == "X" and s[i + 1] in ("L", "C")) or \
            (s[i] == "C" and s[i + 1] in ("D","M")): 
                
                total += romanDict[s[i + 1]] - romanDict[s[i]]
                i += 2
            else: 
                total += romanDict[s[i]]
                i += 1
        else: 
            total += romanDict[s[i]]
            i += 1

    return total


s = "MCMXCIV"

print(romanToInt(s))