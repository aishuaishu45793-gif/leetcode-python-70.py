# Program 139: Sum of Numbers Using Recursion

def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)

number = 5
print("Sum:", sum_numbers(number))