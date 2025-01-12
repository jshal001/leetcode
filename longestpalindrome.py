def longest_palindrome(chars): 
    if len(s) == 1: 
        return 1
    
    char_dict = {}

    #store counts of chars in dict
    for i in s: 
        if i in char_dict.keys():
            char_dict[i] += 1
        
        else: 
            char_dict[i] = 1

    #add up all the counts that are even 
    #add maximum one odd 
    length = 0
    #flag for if one odd has been added
    maxOdd = 0 
    for i in char_dict.values(): 
        if i % 2 == 0:
            length += i

        else: 
            if(maxOdd < char_dict[i]):
                maxOdd = char_dict[i]
        

    return length + maxOdd

s = "a;ldkjfadskjf"

print(longest_palindrome(s))