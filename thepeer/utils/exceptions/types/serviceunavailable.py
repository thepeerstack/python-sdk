from .base import BaseException as error


class ServiceUnavailableException(error):
    """_summary_: ServiceUnavailableException
    _description_: The service unavailable exception for thepeer sdk
    _usage_:
        raise ServiceUnavailableException(errors)
    _example_:
        raise ServiceUnavailableException({message: "apparently our servers are taking a little vacation of reality"})
    """

    def __init__(self, errors):
        super().__init__(errors)
