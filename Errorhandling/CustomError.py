class Error(Exception):
    """Base class for other exceptions"""
    pass


class NotNumberException(Error):
    """value entered is not a number"""

    def __init__(self, message):
        self._message = message
        
    def message(self):
        return self._message
