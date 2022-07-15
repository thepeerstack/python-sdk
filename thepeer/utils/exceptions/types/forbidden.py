from .base import BaseException as error


class ForbiddenException(error):
    """_summary_: ForbiddenException
    _description_: The forbidden exception for thepeer sdk
    _usage_:
        raise ForbiddenException(errors)
    _example_:
        raise ForbiddenException({message: "you shall not pass"})
    """

    def __init__(self, errors):
        super().__init__(errors)
