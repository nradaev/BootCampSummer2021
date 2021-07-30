#https://www.youtube.com/watch?v=rfscVS0vtbw&t=2297s

print("Hello World")

#draw
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

#string
character_name = "John"
character_age = "35"
print("There once was a man named " + character_name + ", ")
print("he was 35 years old.")

character_name = "Mike"
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".")

#functions
phrase = "Giraffe Academy"
print(phrase.upper())

phrase = "Giraffe Academy"
print(phrase.upper().isupper())

phrase = "Giraffe Academy"
print(len(phrase))


phrase = "Giraffe Academy"
print(phrase[3])

phrase = "Giraffe Academy"
print(phrase.index("a"))

phrase = "Giraffe Academy"
print(phrase.replace("Giraffe", "Elephant"))

#numbers
print(-2.0665)
print(3 * (4 + 5))
print(10 % 3)

my_num = -5
print(str(abs (my_num)) + " is my favorite number")

my_num = -5
print(pow(4, 6))

my_num = -5
print(max(4, 6))

print(round(3.7))

#math functions
from math import *
print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))

#input from user
name = input("Enter your name: ")
print("Hello " + name + "!")

#building a basic calculator
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)
print(result)

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)

#madlibs game
day = input ("Enter day of the week: ")
sport = input ("Enter my favorite sport: ")
animal = input("Enter an animal name: ")

print("Today is " + day)
print("I went for " + sport)
print("And I saw a huge " + animal)
