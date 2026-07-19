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

# # 1. Create a basic tuple
fruits = ("apple", "banana", "cherry")
print("Tuple content:", fruits)

# 2. Access elements using zero-based indexing
print("First fruit:", fruits[0])   # Output: apple
print("Last fruit:", fruits[-1])    # Output: cherry

# 3. Check the length of the tuple
print("Total items:", len(fruits))  # Output: 3

# 4. Check the data type
print("Data type:", type(fruits))   # Output: <class 'tuple'>



# Program 4: Find the Sum and Average of Elements in a Tuple

numbers = (10, 20, 30, 40, 50)

total = 0

for i in numbers:
    total += i

average = total / len(numbers)

print("Sum =", total)
print("Average =", average)



# Program 5: Reverse a Tuple

numbers = (10, 20, 30, 40, 50)

reversed_tuple = ()

for i in range(len(numbers) - 1, -1, -1):
    reversed_tuple += (numbers[i],)

print("Original Tuple =", numbers)
print("Reversed Tuple =", reversed_tuple)