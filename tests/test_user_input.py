import unittest
from unittest import mock
from console_io.user_input import get_user_input


class TestUserInput(unittest.TestCase):
    @mock.patch('console_io.user_input.get_input', return_value='1')
    def test_get_user_input_one(self, _):
        func_inputs = [0, 1, 2, 3]
        func_outputs = ['GET_ALL', 'NEXT', 'PREV', 'PREV']

        for index in range(len(func_inputs)):
            func_input = func_inputs[index]
            func_output = func_outputs[index]
            possible_output = get_user_input(func_input)
            self.assertEqual(possible_output, func_output)

    @mock.patch('console_io.user_input.get_input', return_value='2')
    def test_get_user_input_two(self, _):
        func_inputs = [0, 1, 2, 3]
        func_outputs = ['GET_ID', 'GET_ID', 'NEXT', 'NEXT']

        for index in range(len(func_inputs)):
            func_input = func_inputs[index]
            func_output = func_outputs[index]
            possible_output = get_user_input(func_input)
            self.assertEqual(possible_output, func_output)

    @mock.patch('console_io.user_input.get_input', return_value='3')
    def test_get_user_input_three(self, _):
        func_inputs = [0, 1, 2, 3]
        func_outputs = [None, None, 'GET_ID', 'GET_ID']

        for index in range(len(func_inputs)):
            func_input = func_inputs[index]
            func_output = func_outputs[index]
            possible_output = get_user_input(func_input)
            self.assertEqual(possible_output, func_output)

    @mock.patch('console_io.user_input.get_input', return_value='9')
    def test_get_user_input_nine(self, _):
        func_inputs = [0, 1, 2, 3]
        func_outputs = ['EXIT' for _ in range(len(func_inputs))]

        for index in range(len(func_inputs)):
            func_input = func_inputs[index]
            func_output = func_outputs[index]
            possible_output = get_user_input(func_input)
            self.assertEqual(possible_output, func_output)

    @mock.patch('console_io.user_input.get_input', return_value='12')
    def test_get_user_input_unknown(self, _):
        func_inputs = [0, 1, 2, 3]
        func_outputs = [None for _ in range(len(func_inputs))]

        for index in range(len(func_inputs)):
            func_input = func_inputs[index]
            func_output = func_outputs[index]
            possible_output = get_user_input(func_input)
            self.assertEqual(possible_output, func_output)
