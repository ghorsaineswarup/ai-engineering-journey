def is_anagram(right,wrong):
    #if length don't match cant be anargams
    if len(right) != len(wrong):
        return False
    
    count_right = {}
    count_wrong = {}

    #for right
    for letter in right:
        if letter in count_right:
            count_right[letter] += 1
        else:
            count_right[letter] = 1


    #for wrong
    for letter in wrong:
        if letter in count_wrong:
            count_wrong[letter] +=1
        else:
            count_wrong[letter] = 1


    #comprae both
    return count_right == count_wrong

print(is_anagram("cat","act"))
print(is_anagram("rat","car"))     


 