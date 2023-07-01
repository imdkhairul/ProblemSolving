def rmDuplicatesV1(arr,n) :
    # Write your code here
    tempIndex = 0
    tempValue = arr[0]
    for x in range(1, n):
      if arr[x] != tempValue:
        arr[tempIndex + 1] = arr[x]
        tempIndex = tempIndex + 1
        tempValue = arr[x]
    
    if tempIndex != n - 1:
      arr = arr[:-(n - 1 - tempIndex)]
      
    return len(arr)


def rmDuplicatesV2(arr,n) :
    if n == 0 or n == 1:
       return n
    length = 0
    for x in range(n-1):
      if arr[x] != arr[x+1]:
        arr[length] = arr[x]
        length = length + 1
    
    arr[length] = arr[n - 1]
    if length != n - 1:
      arr = arr[:-(n - 1 - length)]
    return length


rmDuplicatesV1([1,1,1,3,3,5,5],7)
rmDuplicatesV1([10,20,30,40,50],5)
rmDuplicatesV1([5,5,10,10,20],5)

rmDuplicatesV2([1,1,1,3,3,5,5],7)
rmDuplicatesV2([10,20,30,40,50],5)
rmDuplicatesV2([5,5,10,10,20],5)

