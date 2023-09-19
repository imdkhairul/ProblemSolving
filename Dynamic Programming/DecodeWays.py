
def numDecodings(str):
    dp = {len(str):1}
    for i in range(len(str) - 1, -1, -1):
        if str[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i+1]
        
        if i + 1 < len(str) and (str[i] == "1" or str[i] == "2" and str[i+1] in "0123456"):
            dp[i] += dp[i + 2]
    return dp[0]

print(numDecodings("1234"))