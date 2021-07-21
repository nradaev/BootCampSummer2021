import unittest

def vowel_counter(word) -> int:
    count = 0
    if type(word) is list:
        for x in word: count += vowel_counter(x)
    elif type(word) is dict:
        for x,y in word.items():
            count += vowel_counter(x)
            count += vowel_counter(y)
    elif type(word) is not str: return count

    vowel = set("aeiou")

    for letter in word:
        if letter in vowel:
            count = count + 1

    return count

def test_int_input(self):
    input = 266
    expected = 0
    actual - vowel_counter(input)
    self.assertEqual(expected, actual)