def find_gcd(a: int, b: int) -> tuple:
    # Validate input
    if not (isinstance(a, int) and isinstance(b, int) and a > 0 and b > 0):
        raise Exception("Both a and b must be positive integers.")

    division_operations = 0

    # Implement the Euclidean Algorithm
    while b != 0:
        a, b = b, a % b
        division_operations += 1

    # Return the GCD and the number of division operations
    return (a, division_operations)

# Example function calls
print(find_gcd(124, 12))  # Expected output: (4, 2)
print(find_gcd(476, 630))  # Expected output: (14, 3)