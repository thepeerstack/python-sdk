from .base import BaseException as error


class UnauthorizedException(error):
    """_summary_: UnauthorizedException
    _description_: The unauthorized exception for thepeer sdk
    _usage_:
        raise UnauthorizedException(errors)
    _example_:
        raise UnauthorizedException({message: "who are you?"})
    """

    def __init__(self, errors):
        super().__init__(errors)
