import unittest
from assignment import *


class TestException(unittest.TestCase):
    # Test the functions in Task 4
    def test_brackets(self):
        # Test whether the match_bracket() function work as expected
        self.assertEqual(
            'SyntaxError: Not a valid expression, brackets mismatched.',
            match_bracket('((2*4)*(3+2)'))
        # here I didn't use assserTrue() because when the function found any mistake in equation, it will return a String to report the error, and the string is True when in bool type
        self.assertEqual(True, match_bracket('(()())'))

    def test_operands(self):
        # Test whether the check_operands() function work as expected
        self.assertEqual(True, check_operands('((1-1)+1)'))
        
        self.assertEqual(
            'SyntaxError: Not a valid expression, wrong number of operands.',
            check_operands('((1)+1)'))
        self.assertEqual(
            'SyntaxError: Not a valid expression, wrong number of operands.',
            check_operands('(4*3*2)'))

        self.assertEqual(
            'SyntaxError: Not a valid expression, operator missing.',
            check_operands('(((2+3)*(4*5))+(1(2+3)))'))
        self.assertEqual(
            'SyntaxError: Not a valid expression, brackets mismatched.',
            check_operands('(2*4)*(3+2)'))
        self.assertEqual(
            'SyntaxError: Not a valid expression, brackets mismatched.',
            check_operands('(2+5)*(4/(2+2)))'))
        
        self.assertEqual(
            'SyntaxError: Not a valid expression, one number missing.',
            check_operands('(1+(1*))')
        )

        self.assertEqual(
            'SyntaxError: Not a valid expression, two numbers missing.',
            check_operands('(1+(*))')
        )

    def test_valid(self):
        # Test whether the check_valid() function work as expected
        self.assertEqual(True, check_valid('(((1+1)-(1*1))/2)'))
        self.assertEqual("TypeError: Not a valid expression, invalid symbol was entered.",
                         check_valid('((5%1)^2)'))


class TestExpression(unittest.TestCase):
    #  Test the functions in Task 2
    def test_suffix(self):
        # Test whether the suffix() function work as expected
        self.assertEqual(['1', '3', '4', '-', '*'],suffix("(1*(3-4))"))



if __name__ == '__main__':
    unittest.main(verbosity=1)