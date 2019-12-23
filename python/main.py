import logging
import sys
from stringManipulation import stringManipulation as encoder


def main():
    inputString = ["aaeeeeebcdffff", "aefrtdddggg", "aertttefze"]
    for str in inputString:
        __result = encoder.stringManipulation(str).get()
        __stdOutMessage = "INPUT: {0} --> OUTPUT: {1}"
        logging.info(__stdOutMessage.format(str, __result))


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    main()
