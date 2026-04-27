
def print_digit(n):
    if n == 0:
        print(0)
        return

    divisor = 1
    while n // divisor >= 10:
        divisor *= 10

    while divisor > 0:
        print(n // divisor)
        n = n % divisor
        divisor = divisor // 10

# Example
print_digit(10)