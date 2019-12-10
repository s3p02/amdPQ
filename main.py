import logging
import sys
from stringManipulation import stringManipulation as encoder

def main():
    inputString = ["aaeeeeebcdffff", "aefrtdddggg", "aertttefze"]
    for str in inputString:
        print("INPUT: {0} --> OUTPUT: {1}".format(str,encoder.stringManipulation(str).get()))

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout,level=logging.INFO)
    main()
