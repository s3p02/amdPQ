import logging


class charTracker:
    def __init__(self, char, count=0):
        self.char = char
        __initMessage1 = "CLASS charTracker - METHOD init - char: {}"
        logging.debug(__initMessage1.format(self.char))
        self.count = count
        __initMessage2 = "CLASS charTracker - METHOD init - count: {}"
        logging.debug(__initMessage2.format(self.count))
