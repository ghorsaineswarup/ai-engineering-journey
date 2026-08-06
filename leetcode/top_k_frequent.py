def top_k_frequent(nums, k):
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    sorted_nums = sorted(counts, key=counts.get, reverse=True)

    return sorted_nums[:k]


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
print(top_k_frequent([1, 1, 1, 2, 2, 3], 1))
print(top_k_frequent([4, 4, 4, 5, 6, 6], 1))