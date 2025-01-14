import numpy as np

def longestCommonSubsequence(text1: str, text2: str):
    x1 = len(text1) + 1
    x2 = len(text2) + 1
    dp = [[0]*x1 for _ in range(x2)]
    for i in range(1, x2):
        for j in range(1, x1):
            if text1[j-1] == text2[i-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max([dp[i][j-1], dp[i-1][j]])
    return dp[i][j]

text1 = "abcde"
text2 = "ace"
ans = longestCommonSubsequence(text1, text2)
print(ans)
