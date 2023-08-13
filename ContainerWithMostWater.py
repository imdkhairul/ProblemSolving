def maxArea(heights):
    result= 0 
    left, right = 0 , len(heights) - 1
    while left < right:
        area = (right - left) * min(heights[left],heights[right])
        result = max(result,area)
        if heights[left] < heights[right]:
            left = left + 1
        else:
            right = right - 1

    return result

print(maxArea([1,8,6,2,5,4,8,3,7]))