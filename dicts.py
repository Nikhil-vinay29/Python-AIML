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