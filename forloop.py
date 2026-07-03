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