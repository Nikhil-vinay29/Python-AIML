# if statement
a = 33
b = 200
if b > a:
  print("b is greater than a")

# if...else statement
a = 33
b = 200
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# if elif...else statement
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
  print("a is greater than b")

# short hand if
a = 5
b = 2
if a > b: print("a is greater than b")

# if with logical operator
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")