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

# Find Sum of All Elements in a List

numbers = [10, 20, 30, 40, 50]

total = 0

for i in numbers:
    total = total + i

print("Sum =", total)

# Count Even and Odd Numbers in a List

numbers = [10, 15, 22, 37, 40, 53]

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even Numbers =", even)
print("Odd Numbers =", odd)


# Find Common Elements Between Two Lists

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = []

for i in list1:
    if i in list2:
        common.append(i)

print("Common Elements =", common)


# Find Positive and Negative Numbers in a List

numbers = [10, -5, 20, -15, 30, -8]

positive = []
negative = []

for i in numbers:
    if i > 0:
        positive.append(i)
    else:
        negative.append(i)

print("Positive Numbers =", positive)
print("Negative Numbers =", negative)