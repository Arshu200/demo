def sum_of_digits_in_binary(n):
    total = 0
    while n > 0:
        total += n % 2  # Add the least significant digit (remainder when divided by 2)
        n //= 2          # Shift right by one digit (integer division by 2)
    
    return total

# Example usage:
n = int(input())
result = sum_of_digits_in_binary(n)
print(result)  # Output will be 4
