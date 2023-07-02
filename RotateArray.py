def arrayRotate(arr,n,k) :
    for x in range(k):
        for y in range(n-1,0,-1):
            arr[y] , arr[y-1] = arr[y-1], arr[y]
    print(arr)

def rightRotate(arr,n) :
    temp = arr[n-1]
    for x in range(n-1,0,-1):
        arr[x] = arr[x-1]
    arr[0] = temp

def arrayRotateV2(arr,n,k) :
    for y in range(k):
        rightRotate(arr,n)
    print(arr)



arrayRotateV2([1,2,3,4,5],5,3)