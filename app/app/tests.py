from django.test import TestCase

from app.calc import addTwoNumbers, subtractTwoNumbers

class CalcTests(TestCase):

    def test_addTwoNumbers(self):
        # Tests that two numbers are added together and return result
        self.assertEqual(addTwoNumbers(3, 8), 11)

    def test_subtractTwoNumbers(self):
        # Tests that two numbers are subtracted together and return result
        self.assertEqual(subtractTwoNumbers(10, 5), 5)