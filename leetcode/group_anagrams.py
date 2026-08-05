def group_anagrams(words):
    groups={}
    for word in words:
        label = ''.join(sorted(word))
        if  label not in groups:
            groups[label] = []
        groups[label].append(word)
    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
