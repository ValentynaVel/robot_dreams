# Task description:
# 1. Створити програму, яка буде очікувати введення тексту від користувача і повідомляти — чи є введений текст “числом” чи “словом”.
# 2. Якщо введений текст “число”, програма має також вказати чи є воно парним чи непарним.
# 3. Якщо це “слово”, програма має вказати його довжину.

user_input = input("Enter number or word: ")

if user_input.isdigit():
    number = int(user_input)
    if number % 2 == 0:
        print("This is number " + str(number) + ". It is even.")
    else:
        print("This is number " + str(number) + ". It is odd.")
else:
    print("This is word. It contains " + str(len(user_input)) + " letters.")

import unittest
from unittest.mock import patch
from io import StringIO
import sys
from analyze_input import analyze_input


class AnalyzeInputTest(unittest.TestCase):

    @patch('builtins.input', return_value='8')
    @patch('sys.stdout', new_callable=StringIO)
    def test_analyze_input_number_even(self, mock_stdout, mock_input):
        analyze_input()
        self.assertEqual(mock_stdout.getvalue().strip(), 'This is number 8. It is even.')

    @patch('builtins.input', return_value='11')
    @patch('sys.stdout', new_callable=StringIO)
    def test_analyze_input_number_odd(self, mock_stdout, mock_input):
        analyze_input()
        self.assertEqual(mock_stdout.getvalue().strip(), 'This is number 11. It is odd.')

    @patch('builtins.input', return_value='Hello')
    @patch('sys.stdout', new_callable=StringIO)
    def test_analyze_input_word(self, mock_stdout, mock_input):
        analyze_input()
        self.assertEqual(mock_stdout.getvalue().strip(), 'This is word. It contains 5 letters.')


if __name__ == '__main__':
    unittest.main()















