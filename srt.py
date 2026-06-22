# reverse string
name = "reverse string"
rev = ""
for i in  name:
    rev += i
print(rev)

# reverse string using slicing
name = "reverse string"     
rev = name[::-1]
print(rev)

# check if string is palindrome
name = "pop"
rev = [::-1]
if name == rev:
    print("YES")
else:
    print("NO")

# length of string

s = input("Enter a string: ")
count = 0

for ch in s:
    count += 1

print("Length:", count)

# number of words in a string
s = input("Enter a sentence: ")

words = s.split()

print("Number of words:", len(words))

# remove spaces from a string

s = input("Enter a string: ")

result = s.replace(" ", "")

print(result)