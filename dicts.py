# Program 1: Create and Print a Dictionary

student = {
    "name": "Nikhil",
    "age": 20,
    "course": "Python"
}

print(student)


# Program 2: Access Dictionary Values

student = {
    "name": "Nikhil",
    "age": 20,
    "course": "Python"
}

print("Name:", student["name"])
print("Age:", student["age"])


# Program 3: Add a New Key-Value Pair

student = {
    "name": "Nikhil",
    "age": 20
}

student["course"] = "Python"

print(student)


# Program 4: Update a Dictionary Value

student = {
    "name": "Nikhil",
    "age": 20
}

student["age"] = 21

print(student)

# Program 5: Remove an Item from Dictionary

student = {
    "name": "Nikhil",
    "age": 20,
    "course": "Python"
}

student.pop("age")

print(student)


#Count Frequency of Elements Using Dictionary

numbers = [1, 2, 2, 3, 3, 3, 4, 4]

frequency = {}

for i in numbers:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print("Frequency =", frequency)


# Program 12: Find Key with the Minimum Value

marks = {
    "Arun": 85,
    "Ravi": 72,
    "Kiran": 90,
    "Rahul": 68
}

lowest_name = ""
lowest_marks = 100

for name in marks:
    if marks[name] < lowest_marks:
        lowest_marks = marks[name]
        lowest_name = name

print("Lowest Student =", lowest_name)
print("Marks =", lowest_marks)