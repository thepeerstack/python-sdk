# the base error for thepeer sdk inheriting from the Exception class
class BaseException(Exception):
    """_summary_: BaseException
    _description_: The base exception for thepeer sdk
    _usage_:
        raise BaseException(errors)
    _example_:
        raise BaseException({message: "an error occurred"})
    """

    def __init__(self, errors={}):
        self.errors = errors

    def __str__(self):
        return self.errors
