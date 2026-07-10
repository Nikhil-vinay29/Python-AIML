# Create a set with unique elements
numbers = {10, 20, 30, 40}

print(numbers)

# Create a set with duplicate elements
numbers = {10, 20, 20, 30, 30, 30}

print(numbers)

# Create an empty set
numbers = set()

print(numbers)

# Add an element to the set
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)

# Update the set with multiple elements
numbers = {10, 20, 30}

numbers.update([40, 50, 60])

print(numbers)

# Remove an element from the set
numbers = {10, 20, 30, 40, 50}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

common = set1.intersection(set2)

print("Common Elements:", common)   

# Check if a set is a subset of another set
set1 = {10, 20, 30}
set2 = {10, 20, 30, 40, 50}

if set1.issubset(set2):
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")

# Check if a set is a superset of another set
set1 = {10, 20, 30, 40, 50}
set2 = {10, 20, 30}

if set1.issuperset(set2):
    print("set1 is a superset of set2")
else:
    print("set1 is not a superset of set2")