import logging
import sys
import unittest
from stringManipulation import stringManipulation as encoder


class testStringManipulation(unittest.TestCase):
    def testGet(self):
        inputString1 = "aaeeeeebcdffff"
        inputString2 = "aefrtdddggg"
        inputString3 = "aertttefze"
        resultString1 = "aaze5bcdzf4"
        resultString2 = "aefrtzd3zg3"
        resultString3 = "aerzt3efze"
        compute1 = encoder.stringManipulation(inputString1).get()
        compute2 = encoder.stringManipulation(inputString2).get()
        compute3 = encoder.stringManipulation(inputString3).get()
        self.assertEqual(compute1, resultString1)
        self.assertEqual(compute2, resultString2)
        self.assertEqual(compute3, resultString3)


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    unittest.main()
