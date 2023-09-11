def knapSack(c,n,wt,val):
    dp = [[0 for x in range(c + 1)] for x in range(n + 1)]
    
    for i in range(n + 1):
        for w in range(c + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w - wt[i - 1]] , dp[i - 1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][c]


def coinChange(self, coins, amount):
    dp = [amount + 1] * (amount+1)
    dp[0] = 0
    for a in range(1,amount+1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a],1 + dp[a-c])
    
    if dp[amount] != (amount + 1):
        return dp[amount]
    else:
        return -1
    
def lengthOfLIS(self, nums):
    dp = [1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i+1, len(nums)):
            if dp[i] < dp[j]:
                dp[i] = max(dp[i],1 + dp[j])

    return max(dp)


print(knapSack(7,4,[1,3,4,5],[1,4,5,7]))
