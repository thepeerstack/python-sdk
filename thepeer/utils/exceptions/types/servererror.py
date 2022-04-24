from .base import BaseException as error


class ServerErrorException(error):
    """_summary_: ServerErrorException
    _description_: The server error exception for thepeer sdk
    _usage_:
        raise ServerErrorException(errors)
    _example_:
        raise ServerErrorException({message: "We played a little bit too much and broke something"})
    """

    def __init__(self, errors):
        super().__init__(errors)
