
def reverse(str) :
    chars = list(str)
    start = 0
    end = len(str) - 1
    while(start < end) :
        if not chars[start].isalpha() :
            start = start + 1
        elif not chars[end].isalpha() :
            end = end - 1
        else :
            chars[end] , chars[start] = chars[start] , chars[end]
            start = start + 1
            end = end - 1
    print("".join(chars))
    return "".join(chars)

reverse("a....bcdee^f")
