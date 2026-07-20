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