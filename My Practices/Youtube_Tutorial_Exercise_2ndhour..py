# https://www.youtube.com/watch?v=rfscVS0vtbw&t=2297s

# Lists when dealing with lots amount of data. How to organize lists.

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
print(friends)


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Karen")
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.remove("Karen")
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends.index("Karen"))

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
print(friends.count("Jim"))

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Jim", "Karen", "Nik", "Toby", "Nadya"]
friends.sort()
print(friends)

# Tupils - container to store different values. Tupils are ummitabel, you can't change them.
coordinates = (4, 5)
print(coordinates[0])

# Functions


def say_hi(name, age):
    print("Hello " + name + ", you are " +age)


say_hi("Nadya", "35")
say_hi("Steve", "30")

# Return Statement (for python function)


def cube(num):
    return num*num*num


print(cube(4))

#If Statements

# I wake up
# If I'm hungry
#    I eat breakfast

#I leave my house
#if it's cloudy
#   I bring an umbrella
#otherwise#
#    I bring sunglasses


is_male = True

if is_male:
    print("You are a male")

is_male = False

if is_male:
    print("You are a male")

is_male = False

if is_male:
    print("You are a male")
else:
    print("You are not a male")

is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")


is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall")