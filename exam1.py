# Function to Welcome the person
def welcomeAboard(name):
    print("Welcome",name)  # Your code here

def printInDecreasing(x):
    # code here
    while (x >= 0):
        print(x, end = " ")
        # your statement below to print the number
        # in decreasing order
        # Note: use end=" " parameter with print to seperate numbers by space.
        ##Output for testcases will automatically separated by a new line by the print() in driver code

        x -= 1

# @param x: int
# @return: string

def checkOddEven(x):
    # code here
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input())

# code here
for i in range(1, 11):
    print(n * i, end = " ")

def friends_in_trouble(j_angry, s_angry):
    if j_angry == s_angry:
        return True
    else:
        return False