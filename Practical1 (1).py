n = int(input("Enter the number of terms: "))

fib = [0, 1]   # Initial two terms
step = 2        # For initialization of fib[0] and fib[1]

# Generate Fibonacci sequence and count steps
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
    step += 3   # 2 index accesses + 1 addition

# Display Fibonacci Series
print("Fibonacci Series:", end=" ")
for i in range(n):
    print(fib[i], end=" ")
    step += 1   # Counting print step

print("\nTotal Step Count =", step)
