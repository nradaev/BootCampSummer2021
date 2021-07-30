# https://www.youtube.com/watch?v=rfscVS0vtbw&t=2297s


# try:
#    value = 10 / 0
#    number = int(input("Enter a number"))
#    print(number)
# except:
#    print("Invalid Input")


# Reading Files (.txt)

# Test_file = open("Test", "r")
# print(Test_file.headlines())
# Test_file.close()
#
# # Writing to files
#
# Test_file = open("Test", "a")
# Test_file.write(" This is Nadya's test file")
# Test_file.close()
#
# # a = append (add) file
# Test_file = open("Test", "a")
# Test_file.write("\nThis is not Kelly's test file")
# Test_file.close()
#
# # w = write a file
# Test_file = open("Test", "w")
# Test_file.write("\nThis is not Chris's test file")
# Test_file.close()
#
# # for new file
# # w = write a new file (it will duplicate file)
# Test_file = open("Test1", "w")
# Test_file.write("\nThis is not Chris's test file")
# Test_file.close()

# Modules in Python

#uilding a multiple choice quizz
from Questions import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)

# Object functions (class function)

# Python Interpreter using command prompt
