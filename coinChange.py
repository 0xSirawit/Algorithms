coins = [1, 2, 5]
amount = 11

def coinChangeBU(coins: list[int], amount: int):
    dp = [float("inf")] * (amount+1)
    dp[0] = 0 

    for i in range(1, amount+1):
        for coin in coins:
            if coin <= i:
                dp[i] = min([dp[i], 1 + dp[i - coin]])

    return -1 if dp[amount] == float("inf") else dp[amount]

print("Problem")
print(f"coins = {coins}")
print(f"amount = {amount}")
ans = coinChangeBU(coins, amount)
print(f"Ans = {ans}")
