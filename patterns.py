# Pattern 1: Square Star Pattern

n = 5

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# Pattern 2: Increasing Star Triangle

n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Pattern 3: Decreasing Star Triangle

n = 5

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# Pattern 4: Number Triangle

n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()