from .base import BaseException as error


class NotFoundException(error):
    """_summary_: NotFoundException
    _description_: The not found exception for thepeer sdk
    _usage_:
        raise NotFoundException(errors)
    _example_:
        raise NotFoundException({message: "you are definitely lost"})
    """

    def __init__(self, errors):
        super().__init__(errors)
