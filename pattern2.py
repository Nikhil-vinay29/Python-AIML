# Pattern 8: Full Pyramid

n = 5

for i in range(1, n + 1):

    # Print spaces
    for j in range(n - i):
        print(" ", end=" ")

    # Print stars
    for k in range(2 * i - 1):
        print("*", end=" ")

    print()# Pattern 9: Inverted Pyramid

n = 5

for i in range(n, 0, -1):

    # Print spaces
    for j in range(n - i):
        print(" ", end=" ")

    # Print stars
    for k in range(2 * i - 1):
        print("*", end=" ")

    print()

# Pattern 10: Diamond Star Pattern

n = 5

# Upper half
for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end=" ")

    for k in range(2 * i - 1):
        print("*", end=" ")

    print()

# Lower half
for i in range(n - 1, 0, -1):

    for j in range(n - i):
        print(" ", end=" ")

    for k in range(2 * i - 1):
        print("*", end=" ")

    print()

# Pattern 11: Number Pyramid

n = 5

for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end=" ")

    for k in range(1, i + 1):
        print(k, end=" ")

    print()


# Pattern 12: Repeated Number Pyramid

n = 5

for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end=" ")

    for k in range(2 * i - 1):
        print(i, end=" ")

    print()



# Pattern 16: Alphabet Triangle

n = 5

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()