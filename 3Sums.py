def threeSum(nums):
    res = []
    nums.sort()
    
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1
        while left < right:
            three = a + nums[left] + nums[right]
            if three < 0:
                left = left + 1
            elif three > 0:
                right = right - 1
            else:
                res.append([a,nums[left],nums[right]])
                left = left + 1
                while nums[left] == nums[left - 1] and left < right:
                    left = left + 1
    
    return res
    

print(threeSum([-1,0,1,2,-1,-4]))