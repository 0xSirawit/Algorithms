# Bottom Up Approach (Tabulation)
def fiboBU(n: int):
    dp = [0]*(n+1)
    if n != 0:
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Top Down Approach (Memoization)
def fiboTD(n: int, memo: list[int]):
    if n <= 1: return n
    if n in memo: return memo[n]
    memo[n] = fiboTD(n-1, memo) + fiboTD(n-2, memo)
    return memo[n]

n = int(input("n = "))
memo = [0]*(n+1)
print(f'Fn = {fiboTD(n, memo)}')
print(f'Fn = {fiboBU(n)}')
