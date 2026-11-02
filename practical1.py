# Non-recursive (Iterative) method
def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Recursive method
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


n = int(input("Enter number of terms: "))

print("\nNon-recursive Fibonacci:")
fibonacci_iterative(n)

print("\n\nRecursive Fibonacci:")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")


# Complexity Analysis
print("\n\n--- Complexity Analysis ---")

print("Iterative Method:")
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")

print("\nRecursive Method:")
print("Time Complexity: O(2^n)")
print("Space Complexity: O(n)")