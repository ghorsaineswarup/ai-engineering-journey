def contains_duplicate(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return True
        seen[num] = True
    return False


print(contains_duplicate([1, 2, 2, 3]))    
print(contains_duplicate([1, 2, 3, 4]))    