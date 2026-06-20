# print string
print("This is a string")

# length of string
print(len("Nikhil" ))

# upper case to lower case
print("NIKHIL".lower())

# lower case to upper case
print("nikhil".upper())

# count vowels in a string
s = input().lower()
count = 0

for ch in s:
    if ch in "aeiou":
        count += 1

print(count)