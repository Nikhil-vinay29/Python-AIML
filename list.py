# Find the largest and smallest number in a list
numbers = [12, 45, 7, 89, 23]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest =", largest)
print("Smallest =", smallest)


# Remove duplicates from a list
numbers = [1, 2, 2, 3, 4, 4, 5]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print(unique)

numbers = [10, 45, 23, 89, 67]

largest = numbers[0]
second = numbers[0]

# Find the second largest number in a list
for i in numbers:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second Largest =", second)