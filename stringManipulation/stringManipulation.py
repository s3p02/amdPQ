import logging

class stringManipulation:
    __charCache = ""
    def __init__(self,inputString,threshold=9):
        self.inputString = inputString
        logging.debug("CLASS stringManipulation - METHOD init - inputString: {}".format(self.inputString))
        self.threshold = threshold
        logging.debug("CLASS stringManipulation - METHOD init - threshold: {}".format(self.threshold))
        self.__getCache()
    def __checkThreshold(self,count):
        if count < self.threshold:
            logging.debug("CLASS stringManipulation - METHOD __checkThreshold - count < threshold : {0} < {1}".format(count,self.threshold))
            return count
        else:
            logging.debug("CLASS stringManipulation - METHOD __checkThreshold - count > threshold : {0} < {1}".format(count,self.threshold))
            return self.threshold
    def __getCache(self):
        prevChar = charTracker(self.inputString[0],1)
        logging.debug("CLASS stringManipulation - METHOD __getCache - BEGIN! prevChar => {0}:{1}".format(prevChar.char,prevChar.count))
        for character in range(1,len(self.inputString),1):
            logging.debug("CLASS stringManipulation - METHOD __getCache - Iteration:{0} prevChar => {1}:{2}".format(character,prevChar.char,prevChar.count))
            currChar = self.inputString[character]
            logging.debug("CLASS stringManipulation - METHOD __getCache - Iteration:{0} currChar : {1}".format(character,currChar))
            if prevChar.char == currChar:
                logging.debug("CLASS stringManipulation - METHOD __getCache - Matching! prevChar == currChar : {0} == {1}".format(prevChar.char,currChar))
                prevChar.count += 1
                logging.debug("CLASS stringManipulation - METHOD __getCache - Matching! prevChar:prevCharCount : {0} == {1}".format(prevChar.char,prevChar.count))
            else:
                self.__charCache += "z"+prevChar.char+str(self.__checkThreshold(prevChar.count))
                logging.debug("CLASS stringManipulation - METHOD __getCache - Not-Matching! __charCache : {}".format(self.__charCache))
                prevChar = charTracker(currChar,1)
                logging.debug("CLASS stringManipulation - METHOD __getCache - Not-Matching! prevChar:prevCharCount => {0}:{1}".format(prevChar.char,prevChar.count))
        self.__charCache += "z"+prevChar.char+str(self.__checkThreshold(prevChar.count))
        logging.debug("CLASS stringManipulation - METHOD __getCache - END! __charCache : {}".format(self.__charCache))
    def get(self):
        result = self.__charCache
        logging.debug("CLASS stringManipulation - METHOD get - result: {}".format(result))
        return result
