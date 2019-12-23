import logging
from charTracker import charTracker as ct


class stringManipulation:
    __charCache = ""

    def __init__(self, inputString, threshold=9):
        self.inputString = inputString
        __initMessage1 = "stringManipulation - init - inputString: {}"
        logging.debug(__initMessage1.format(self.inputString))
        self.threshold = threshold
        __initMessage2 = "stringManipulation - init - threshold: {}"
        logging.debug(__initMessage2.format(self.threshold))
        self.__getCache()

    def __checkThreshold(self, count):
        if count < self.threshold:
            __thresholdMessage1 = "stringManipulation threshold {0} < {1}"
            logging.debug(__thresholdMessage1.format(count, self.threshold))
            return count
        else:
            __thresholdMessage2 = "stringManipulation threshold {0} < {1}"
            logging.debug(__thresholdMessage2.format(count, self.threshold))
            return self.threshold

    def __repeatAndReturnChar(self, char, charCount):
        __retCharMessage1 = "stringManipulation - char:{0} - charCount:{1}"
        logging.debug(__retCharMessage1.format(char, charCount))
        returnChar = ''.join([ichar*charCount for ichar in char])
        __retCharMessage2 = "stringManipulation - returnChar:{}"
        logging.debug(__retCharMessage2.format(returnChar))
        return returnChar

    def __finalCharCheck(self, char, threshold):
        if threshold <= 2:
            return self.__repeatAndReturnChar(char, threshold)
        else:
            return "z"+char+str(threshold)

    def __getCache(self):
        prevChar = ct.charTracker(self.inputString[0], 1)
        __cacheMessage1 = "stringManipulation - BEGIN! prevChar => {0}:{1}"
        logging.debug(__cacheMessage1.format(prevChar.char, prevChar.count))
        for character in range(1, len(self.inputString), 1):
            __cm2 = "stringManipulation - Iter:{0} prevChar => {1}:{2}"
            logging.debug(__cm2.format(character,
                                       prevChar.char,
                                       prevChar.count))
            currChar = self.inputString[character]
            __cm3 = "stringManipulation - Iter:{0} currChar : {1}"
            logging.debug(__cm3.format(character, currChar))
            if prevChar.char == currChar:
                __cm4 = "stringManipulation - Matching! {0} == {1}"
                logging.debug(__cm4.format(prevChar.char, currChar))
                prevChar.count += 1
                __cm5 = "stringManipulation - Matching! {0}({1})"
                logging.debug(__cm5.format(prevChar.char, prevChar.count))
            else:
                if prevChar.count <= 2:
                    self.__charCache += self.__repeatAndReturnChar(prevChar.char, prevChar.count)
                else:
                    self.__charCache += "z"+prevChar.char+str(self.__checkThreshold(prevChar.count))
                    __cm6 = "stringManipulation - Not-Matching! {}"
                    logging.debug(__cm6.format(self.__charCache))
                prevChar = ct.charTracker(currChar, 1)
                __cm7 = "stringManipulation - Not-Matching! {0}({1})"
                logging.debug(__cm7.format(prevChar.char, prevChar.count))
        fCharThresholdCheck = self.__checkThreshold(prevChar.count)
        self.__charCache += self.__finalCharCheck(prevChar.char, fCharThresholdCheck)
        __cm8 = "stringManipulation - END! {}"
        logging.debug(__cm8.format(self.__charCache))

    def get(self):
        result = self.__charCache
        __getMessage = "stringManipulation - get - result: {}"
        logging.debug(__getMessage.format(result))
        return result
