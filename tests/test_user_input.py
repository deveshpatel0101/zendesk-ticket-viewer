import unittest
from unittest.mock import patch
from user_input import get_user_input, is_valid_input


class TestUserInput(unittest.TestCase):
    @patch('user_input.get_input', return_value='1')
    def test_get_user_input_one(self, _):
        func_inputs = [None, 'GET_ALL', 'GET_ID', 'PREV', 'NEXT']
        func_outputs = ['GET_ALL', 'PREV', 'GET_ALL', 'PREV', 'PREV']

        for index in range(len(func_inputs)):
            func_input = func_inputs[index]
            func_output = func_outputs[index]
            possible_output = get_user_input(func_input)
            self.assertEqual(possible_output, func_output)

    @patch('user_input.get_input', return_value='2')
    def test_get_user_input_two(self, _):
        func_inputs = [None, 'GET_ALL', 'GET_ID', 'PREV', 'NEXT']
        func_outputs = ['GET_ID', 'NEXT', 'GET_ID', 'NEXT', 'NEXT']

        for index in range(len(func_inputs)):
            func_input = func_inputs[index]
            func_output = func_outputs[index]
            possible_output = get_user_input(func_input)
            self.assertEqual(possible_output, func_output)

    @patch('user_input.get_input', return_value='3')
    def test_get_user_input_three(self, _):
        func_inputs = [None, 'GET_ALL', 'GET_ID', 'PREV', 'NEXT']
        func_outputs = [None, 'GET_ID', None, 'GET_ID', 'GET_ID']

        for index in range(len(func_inputs)):
            func_input = func_inputs[index]
            func_output = func_outputs[index]
            possible_output = get_user_input(func_input)
            self.assertEqual(possible_output, func_output)

    @patch('user_input.get_input', return_value='9')
    def test_get_user_input_nine(self, _):
        func_inputs = [None, 'GET_ALL', 'GET_ID', 'PREV', 'NEXT']
        func_outputs = ['EXIT' for _ in range(len(func_inputs))]

        for index in range(len(func_inputs)):
            func_input = func_inputs[index]
            func_output = func_outputs[index]
            possible_output = get_user_input(func_input)
            self.assertEqual(possible_output, func_output)

    @patch('user_input.get_input', return_value='12')
    def test_get_user_input_unknown(self, _):
        func_inputs = [None, 'GET_ALL', 'GET_ID', 'PREV', 'NEXT']
        func_outputs = [None for _ in range(len(func_inputs))]

        for index in range(len(func_inputs)):
            func_input = func_inputs[index]
            func_output = func_outputs[index]
            possible_output = get_user_input(func_input)
            self.assertEqual(possible_output, func_output)

    def test_is_valid_input(self):
        func_inputs = [('PREV', 1, None), ('PREV', 0, None),
                       ('PREV', 2, None), ('NEXT', 0, False), ('NEXT', 0, True)]
        func_outputs = [False, False, True, False, True]
        for index in range(len(func_inputs)):
            func_input = func_inputs[index]
            func_output = func_outputs[index]
            possible_output = is_valid_input(
                func_input[0], func_input[1], func_input[2])
            self.assertEqual(possible_output, func_output)
