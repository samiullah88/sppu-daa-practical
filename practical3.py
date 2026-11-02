
n = int(input("Enter number of items: "))
items = []

for i in range(n):
    weight = float(input("Enter weight: "))
    profit = float(input("Enter profit: "))
    items.append((profit / weight, weight, profit, i + 1))

capacity = float(input("Enter bag capacity: "))
total_capacity = capacity
total_profit = 0

items.sort(reverse=True)

for ratio, weight, profit, item_no in items:
    if capacity <= 0:
        break

    taken = min(weight, capacity)
    fraction = taken / weight
    earned = profit * fraction

    total_profit += earned
    capacity -= taken

    print(f"Item {item_no}: Took {fraction * 100:.2f}%")

print("Maximum Profit:", total_profit)
print("Remaining Capacity:", capacity)
print("Bag Percentage Left:", capacity / total_capacity * 100, "%")
print("Bag Percentage Filled:",
      (total_capacity - capacity) / total_capacity * 100, "%")
