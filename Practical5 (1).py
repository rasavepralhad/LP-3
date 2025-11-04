# Binomial Coefficients using Dynamic Programming

def binomial_coeff(n, k):
    # Step 1: Create a 2D table
    C = [[0 for x in range(k+1)] for y in range(n+1)]

    # Step 2: Fill the table using DP relation
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]

    return C[n][k]


# Driver Code
n = int(input("Enter n: "))
k = int(input("Enter k: "))

print(f"Binomial Coefficient C({n}, {k}) =", binomial_coeff(n, k))
