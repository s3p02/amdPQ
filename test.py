import logging
import sys
import unittest
from stringManipulation import stringManipulation as encoder


class testStringManipulation(unittest.TestCase):
    def testGet(self):
        inputString = "aaeeeeebcdffff"
        resultString = "za2ze5zb1zc1zd1zf4"
        compute = encoder.stringManipulation(inputString).get()
        self.assertEqual(compute, resultString)


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    unittest.main()
