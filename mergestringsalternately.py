def merge_words(word1, word2): 
    
    i = 0
    finalWord = ""
    while i < len(word1) and i < len(word2): 
        finalWord += word1[i] + word2[i]
        i += 1

    if i == len(word1):
        finalWord += word2[i:]
    elif i == len(word2): 
        finalWord += word1[i:]
    
    return finalWord


word1 = "abcdef"
word2 = "pqr"

print(merge_words(word1, word2))