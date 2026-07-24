# Program 6: Find the Maximum and Minimum Difference in a Tuple

numbers = (12, 45, 7, 89, 23)

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

difference = largest - smallest

print("Largest =", largest)
print("Smallest =", smallest)
print("Difference =", difference)


# Program 7: Check Whether an Element Exists in a Tuple

numbers = (10, 20, 30, 40, 50)

element = int(input("Enter the element to search: "))

found = False

for i in numbers:
    if i == element:
        found = True
        break

if found:
    print(element, "is present in the tuple.")
else:
    print(element, "is not present in the tuple.")


# Program 8: Find the Index of an Element in a Tuple (Without Using index())

numbers = (10, 20, 30, 40, 50)

element = int(input("Enter the element to find: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == element:
        print("Index =", i)
        found = True
        break

if not found:
    print("Element not found")


# Program 9: Count Even and Odd Numbers in a Tuple

numbers = (12, 7, 18, 25, 30, 41, 56)

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even Numbers =", even)
print("Odd Numbers =", odd)