from .base import BaseException as error


class NotAcceptableException(error):
    """_summary_: NotAcceptableException
    _description_: The not acceptable exception for thepeer sdk
    _usage_:
        raise NotAcceptableException(errors)
    _example_:
        raise NotAcceptableException({message: "you need to work to get some money"})
    """

    def __init__(self, errors):
        super().__init__(errors)
