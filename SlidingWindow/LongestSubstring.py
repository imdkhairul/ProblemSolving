# Longest Substring Without Repeating Characters

def lengthOfLongestSubstring(s):
    l = 0
    res = 0
    charSet = set()
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l = l + 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res

print(lengthOfLongestSubstring("abcabcbb"))
