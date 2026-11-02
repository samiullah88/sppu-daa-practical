
# 0-1 Knapsack using Dynamic Programming

n = int(input("Enter number of items: "))

weights = []
profits = []

for i in range(n):
    print(f"\nItem {i + 1}")
    weight = int(input("Enter weight: "))
    profit = int(input("Enter profit: "))
    weights.append(weight)
    profits.append(profit)

W = int(input("\nEnter bag capacity: "))

# Create DP table
dp = [[0] * (W + 1) for _ in range(n + 1)]

# Fill DP table
for i in range(1, n + 1):
    for w in range(W + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(
                profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

# Display DP table
print("\n--- Dynamic Programming Table ---")
print("Item/Capacity", end="\t")
for w in range(W + 1):
    print(w, end="\t")
print()

for i in range(n + 1):
    print(i, end="\t\t")
    for w in range(W + 1):
        print(dp[i][w], end="\t")
    print()

# Find selected items
selected = []
w = W

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected.append(i)
        w -= weights[i - 1]

selected.reverse()

used_weight = sum(weights[i - 1] for i in selected)
remaining = W - used_weight
maximum_profit = dp[n][W]

# Display results
print("\n--- Final Results ---")
print("Selected Items:", selected)
print("Maximum Profit:", maximum_profit)
print("Bag Capacity:", W)
print("Weight Used:", used_weight)
print("Remaining Capacity:", remaining)

if W > 0:
    print("Bag Filled:", round(used_weight / W * 100, 2), "%")
    print("Bag Left:", round(remaining / W * 100, 2), "%")
else:
    print("Bag Filled: 0%")
    print("Bag Left: 0%")
