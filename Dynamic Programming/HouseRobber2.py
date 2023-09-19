def rob(nums):
    return max(nums[0],helper(nums[1:]),helper(nums[:-1]))

def helper(nums):
    rob1, rob2 = 0, 0
    for n in nums:
        newrob = max((rob1 + n) ,rob2)
        rob1 = rob2
        rob2 = newrob
    return rob2

def numDecodings(str):
    dp = {len(str):1}
    for i in range(len(str) - 1, -1, -1):
        if str[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i+1]
        
        if i + 1 < len(str) and str[i] == "1" or str[i] == "2" and str[i+1] in "0123456":
            dp[i] += dp[i + 2]
    return dp

print(numDecodings("1234"))