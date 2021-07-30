# https://www.youtube.com/watch?v=rfscVS0vtbw&t=2297s

# If Statements & Comparisons

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(3, 40, 5))

# == if both are equal
# != not equal to

# Building a Better Calculator

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")


#Using Dictionaries
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April"

}

print(monthConversions["Mar"])

# or use print(monthConversions.get("Dec"))

# While loop
i = 1
while i <= 10:
    print(i)
    i += 1

print ("Done with loop")

# For Loop
friends = ["Jim", "Karen", "Kevin"]
for name in friends:
    print(name)

friends = ["Jim", "Karen", "Kevin"]
for index in range(len(friends)):
    print(friends[index])

friends = ["Jim", "Karen", "Kevin"]
for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("not first")

# Exponent Function
print(2**3)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(3, 4))

# 2D Lists
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0])

for row in number_grid:
    for col in row:
        print(col)

# Build a Translator
# Exsample: Giraffe Language
#vowels -> g
#-------------
#dog -> dgg
#cat -> cgt

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter

    return translation

print(translate(input("Enter a phrase")))

# Comments in python use # (hashtags)

