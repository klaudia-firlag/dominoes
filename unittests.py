import unittest
from run_dominoes import Dominoes


class TestDominoes(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestDominoes, self).__init__(*args, **kwargs)
        self.dominoes = Dominoes()

    def test_input_empty(self):
        in_string = ''
        self.assert_raises_exception(in_string)

    def test_input_too_short(self):
        in_string = '/'
        self.assert_raises_exception(in_string)

    def test_input_invalid_chars(self):
        in_string = '/a9'
        self.assert_raises_exception(in_string)

    def test_input_invalid_num_iter(self):
        in_string = '/||||'
        num_iter = -1
        self.assert_raises_exception(in_string, num_iter)

    def assert_raises_exception(self, in_string, num_iter=1):
        with self.assertRaises(Exception):
            self.dominoes.forward(in_string, num_iter)
        with self.assertRaises(Exception):
            self.dominoes.backward(in_string, num_iter)

    def test_forward_2iterations(self):
        in_string = '||/||||\\|/\\|'
        expected_output = '||///\\\\\\|/\\|'
        num_iter = 2

        result = self.dominoes.forward(in_string, num_iter)

        self.assertIsInstance(result, str)
        self.assertEqual(result, expected_output)

    def test_backward_2iterations(self):
        in_string = '||////\\\\\\|////|'
        expected_output = '||//||||\\|//|||'
        num_iter = 2

        result = self.dominoes.backward(in_string, num_iter)

        self.assertIsInstance(result, str)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
