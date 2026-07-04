# This is a simple for loop that prints numbers from 1 to 10.
for i in range(1, 11):
    print(i)
# This is a simple for loop that prints numbers from 10 to 1 in reverse order.
for i in range(10, 0, -1):
    print(i)
# This is a simple for loop that prints even numbers from 2 to 50.
for i in range(2, 51, 2):
    print(i)   

# This is a simple for loop that prints odd numbers from 1 to 49.
for i in range(1, 50, 2):
    print(i)    

# This is a simple for loop that calculates the factorial of a number entered by the user.
n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print("Factorial =", factorial)

# This is a simple for loop that prints the Fibonacci series up to n terms entered by the user.
n = int(input("Enter the number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

# This is a simple for loop that calculates the sum of squares of numbers from 1 to n entered by the user.

n = int(input("Enter N: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + (i * i)

print("Sum of Squares =", sum)

# This is a simple for loop that prints the common factors of two numbers entered by the user.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Common Factors are:")

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        print(i)

# This is a simple for loop that counts the number of prime numbers up to n entered by the user.
n = int(input("Enter N: "))

count = 0

for i in range(2, n + 1):
    prime = True

    for j in range(2, i):
        if i % j == 0:
            prime = False
            break

    if prime:
        count = count + 1

print("Total Prime Numbers =", count)