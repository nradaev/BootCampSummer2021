#   *
#  ***
# *****
#   |


# height_of_tree = 3
# print(' '*3' + 'x)
# print(' '*2 + 'x'*3)
# print(' ' + 'x'*5)
import random


def make_tree(height_of_tree: int = random.randint(2, 12), symbol: str = '*'):
    for branch in range(height_of_tree):
        # max = height_of_tree * 2
        print(' ' * (height_of_tree - branch) + symbol * (1 + (branch * 2)))
        # print(' ' * (height_of_tree - branch) + symbol * (max - (max - (branch*2) -1)))
    print(' ' * height_of_tree + '|')


make_tree(4)
make_tree(7, '$')


def register(name, gender=None, race='', *other, **stuff):
    print(f"Hello {name}!")
    if gender:
        print(f"You are a {gender}!")
    if race:
        print(f"Your race is '{race}")
    for i in other:
        print(f"... and you are {i}")

    for (k, v) in stuff.items():
        print(f"... your {k} is {v}")

register('Jane')
register('Bob' , 'male')
register('Jessica', None, 'hispanic', 21, 'white', height=170, cell='408-888-1111')

register(
    race='white',
    gender='male',
    address="123 Apple Ln. Tree, CA",
    name='Steve'
)