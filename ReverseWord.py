def reverse_words(str) :
    temp = []
    finalString = ""
    for i in range(len(str)) :
        if str[i] == " " :
           while(len(temp) > 0):
               finalString = finalString + temp.pop()
               if len(temp) == 0 :
                   finalString = finalString + " "
        else:
           temp.append(str[i])

    while(len(temp) > 0):
        finalString = finalString + temp.pop()
    
    str = finalString
    print(str)


def reverse_wordsV2(str) :
    wStart = 0
    length = len(str)
    chars = list(str)
    for i in range(length) :
        if str[i] == " " :
           reverse(chars,wStart,i - 1)
           wStart = i + 1

    reverse(chars,wStart,length - 1)
    str = ''.join(chars)
    print(str)

def reverse(arr, start, end) :
    while(start<end) :
        temp = arr[start]
        arr[start] = arr[end]
        start = start + 1
        arr[end] = temp
        end = end - 1

reverse_words("Programming is an Art ")
reverse_wordsV2("Programming is an Art ")