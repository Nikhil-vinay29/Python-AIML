# Program 1: Find the Largest and Smallest Element in a Tuple

numbers = (12, 45, 7, 89, 23)

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest =", largest)
print("Smallest =", smallest)



# Program 2: Count the Occurrences of an Element in a Tuple

numbers = (10, 20, 30, 20, 40, 20)
element = 20

count = 0

for i in numbers:
    if i == element:
        count += 1

print(element, "appears", count, "times")


# Program 3: Find the Second Largest Element in a Tuple

numbers = (15, 8, 42, 27, 35)

largest = numbers[0]
second = numbers[0]

for i in numbers:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second Largest =", second)