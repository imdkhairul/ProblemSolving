def reverse(arr, start, end) :
    while(start<end) :
        temp = arr[start]
        arr[start] = arr[end]
        start = start + 1
        arr[end] = temp
        end = end - 1
    

def arrayRotate(arr, n, k) :
    reverse(arr, 0, n - k - 1)
    reverse(arr, n - k, n - 1)
    reverse(arr, 0, n - 1)
    print(arr)

arrayRotate([1,2,3,4,5],5,2)