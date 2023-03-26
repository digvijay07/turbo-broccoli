# Identify Odd and Even from the given number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# get user input
num = int(input("Enter a number: "))

# check if the number is odd or even
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# check if the number is prime
if is_prime(num):
    print(num, "is prime")
else:
    print(num, "is not prime")
