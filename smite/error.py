class SmiteException(Exception):

    """
    Base exception for the library
    Catching this catches all exceptions raised by this library
    """

    pass


class NoResult(SmiteException):

    """
    Raised when a result was not given by a function
    """

    pass


class HTTPError(SmiteException):

    """
    Raised when a problem occurs with HTTP requests
    """

    pass
