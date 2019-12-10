import logging


class charTracker:
    def __init__(self, char, count=0):
        self.char = char
        logging.debug("CLASS charTracker - METHOD init - char: {}".format(self.char))
        self.count = count
        logging.debug("CLASS charTracker - METHOD init - count: {}".format(self.count))
