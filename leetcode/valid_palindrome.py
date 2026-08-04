def is_palindrome(s):
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned = cleaned + char.lower()
    
    reversed_string = cleaned[::-1]
    
    return cleaned == reversed_string


print(is_palindrome("race a car"))
print(is_palindrome("A man, a plan, a canal: Panama"))