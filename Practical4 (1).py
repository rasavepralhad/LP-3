# 0–1 Knapsack Problem using Dynamic Programming

# Step 1: Input number of items
n = int(input("Enter number of items: "))

# Step 2: Take weight and value for each item
weights = []
values = []

for i in range(n):
    value = int(input(f"Enter value of item {i+1}: "))
    weight = int(input(f"Enter weight of item {i+1}: "))
    values.append(value)
    weights.append(weight)

# Step 3: Input maximum capacity of knapsack
W = int(input("Enter capacity of knapsack: "))

# Step 4: Create DP table
# dp[i][w] = max value for first i items with capacity w
dp = [[0 for x in range(W + 1)] for y in range(n + 1)]

# Step 5: Fill DP table
for i in range(1, n + 1):
    for w in range(1, W + 1):
        if weights[i-1] <= w:
            dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]

# Step 6: Print result
print("\nMaximum value in knapsack =", dp[n][W])
