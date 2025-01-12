def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """

    magDict = {}

    for val in magazine:
        if val in magDict:
            magDict[val] += 1
        else:
            magDict[val] = 1

    
    for x in ransomNote:
        if(x in magDict and magDict[x] > 0):
            magDict[x] -= 1
        else:
            return False
        
    return True


magazine = 'ab'
ransomNote = 'aa'

print(canConstruct(ransomNote, magazine))

