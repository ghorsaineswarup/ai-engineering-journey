def longest_substring(s):
    char_set = set()
    left = 0
    best_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        
        current_length = right - left + 1
        best_length = max(best_length, current_length)
    
    return best_length


print(longest_substring("abcabcbb"))   # 3
print(longest_substring("bbbbb"))      # 1
print(longest_substring("pwwkew"))     # 3
print(longest_substring("tmmzuxt"))    # 5