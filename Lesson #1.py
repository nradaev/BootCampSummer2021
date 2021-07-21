import unittest

def find_sum(number1, number2) -> int:
    if number1 == None:
        number1 = 0
    if number2 == None:
        number2 = 0

    if type(number1) == str
        raise ValueError('Please input values')
    return number1 + number2


class MyTestCase(unittest.TestCase):
    def test_something(self):...

    def test_positive_valid_sum(self):
        self.assertEqual(10, find_sum(7, 3))

    def test_none_input(self):
        self.assertLessEqual(5, find_sum(5, None))

    def  test_negative_char_input(self):
        self.assertRaises(ValueError, lambda: find_sum('a' , 'x'))

    def test_negative_char_number_input(self):
            result = find_sum('4', 'x'))



        my_name: str = "Nadya Radaev"
        age: int = 29
        height: float

        name_length = len(my_name) - 1

        self.assertTrue(name_length * 2 < age)
        self.assertLess(name_length < age / 2)




        # self.assertEqual(True, True)





if __name__ == '__main__':
    unittest.main()