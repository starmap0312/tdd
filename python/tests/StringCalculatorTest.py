import unittest
from module.StringCalculator import StringCalculator

class StringCalculatorTest(unittest.TestCase):

    # Requirement 1: The method can take 0-2 numbers separated by comma
    def testWhen2NumbersAreUsedThenNoExceptionIsThrown(self):
        StringCalculator.add("1,2")
        self.assertTrue(True)

    def testWhenNonNumberIsUsedThenExceptionIsThrown(self):
        self.assertRaises(ValueError, StringCalculator.add, "1,X")

    # Requirement 2: For an empty string the method will return 0
    def testWhenEmptyStringIsUsedThenReturnValueIs0(self):
        self.assertEqual(0, StringCalculator.add(""))

    # Requirement 3: Method will return their sum of numbers
    def testWhenOneNumberIsUsedThenReturnValueIsThatSameNumber(self):
        self.assertEqual(3, StringCalculator.add("3"))

    def testWhenTwoNumbersAreUsedThenReturnValueIsTheirSum(self):
        self.assertEqual(3 + 6, StringCalculator.add("3,6"))

    # Requirement 4: Allow the Add method to handle an unknown amount of numbers
    def testWhenAnyNumberOfNumbersIsUsedThenReturnValuesAreTheirSums(self):
        self.assertEqual(3 + 6 + 15 + 18 + 46 + 33, StringCalculator.add("3,6,15,18,46,33"))

    # Requirement 5: Allow the Add method to handle new lines between numbers
    def testWhenNewLineIsUsedBetweenNumbersThenReturnValuesAreTheirSums(self):
        self.assertEqual(3 + 6 + 15, StringCalculator.add("3,6\n15"))

    # Requirement 6: Negative numbers will throw an exception
    def testWhenNegativeNumberIsUsedThenRuntimeExceptionIsThrown(self):
        self.assertRaises(RuntimeError, StringCalculator.add, "3,-6,15,18,46,33")

    # Requirement 7: Numbers bigger than 1000 should be ignored
    def testWhenOneOrMoreNumbersAreGreaterThan1000IsUsedThenItIsNotIncludedInSum(self):
        self.assertEqual(3 + 1000 + 6, StringCalculator.add("3,1000,1001,6,1234"))

if __name__ == "__main__":
    unittest.main()
