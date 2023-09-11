def missingNumber(nums):
    res = len(nums)
    for i in range(len(nums)):
        res = res + (i - nums[i])
    
    return res



def missingNumberV2(nums):
    res = len(nums)
    for i in range(len(nums)):
        res = res ^ (i ^ nums[i])
    return res

print(missingNumberV2([9,6,4,2,3,5,7,0,1]))