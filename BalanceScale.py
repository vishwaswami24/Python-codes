def can_balance_scale(weights):
    total_sum = sum(weights)

    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2
    n = len(weights)

    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]

    # Base case: an empty set can sum to 0
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(target_sum + 1):
            # If we don't include the current weight
            dp[i][j] = dp[i - 1][j]

            # If we include the current weight and the sum is not exceeded
            if j >= weights[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - weights[i - 1]]

    return dp[n][target_sum]

c = can_balance_scale([12,5,4,3])
print(c)