from collections import namedtuple
from enum import Enum


ErrorCode = namedtuple('ErrorCode', 'code error_code')


class WebDriverError(Enum):
    NO_DEVICE_CONNECT_COMPUTER = ErrorCode(1, 'no device connect to computer')


def find_exception_by_code(code):
    error_name = None
    for error in WebDriverError:
        if error.value.code == code:
            error_name = error
            break
    return error_name


class WebDriverException(Exception):

    def __init__(self, error=None, message=None, screen=None, stacktrace=None):
        self.error = error
        self.message = message
        self.screen = screen
        self.stacktrace = stacktrace

    def __str__(self):
        execption_msg = ("\nError:{0}\nMessage:{1}\n").format(self.error, self.message)
        if self.screen is not None:
            execption_msg += "Screenshot: available via screen\n"
        if self.stacktrace is not None:
            stacktrace = "\n".join(self.stacktrace)
            execption_msg += "Stacktrace:\n%s" % stacktrace
        return execption_msg
