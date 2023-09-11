def lengthOfLIS(self, nums):
    dp = [1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i+1, len(nums)):
            if dp[i] < dp[j]:
                dp[i] = max(dp[i],1 + dp[j])

    return max(dp)

print()