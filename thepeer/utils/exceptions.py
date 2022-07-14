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

class ForbiddenException(BaseException):
    """_summary_: ForbiddenException
    _description_: The forbidden exception for thepeer sdk
    _usage_:
        raise ForbiddenException(errors)
    _example_:
        raise ForbiddenException({message: "you shall not pass"})
    """

    def __init__(self, errors):
        super().__init__(errors)

class NotAcceptableException(BaseException):
    """_summary_: NotAcceptableException
    _description_: The not acceptable exception for thepeer sdk
    _usage_:
        raise NotAcceptableException(errors)
    _example_:
        raise NotAcceptableException({message: "you need to work to get some money"})
    """

    def __init__(self, errors):
        super().__init__(errors)


class NotFoundException(BaseException):
    """_summary_: NotFoundException
    _description_: The not found exception for thepeer sdk
    _usage_:
        raise NotFoundException(errors)
    _example_:
        raise NotFoundException({message: "you are definitely lost"})
    """

    def __init__(self, errors):
        super().__init__(errors)


class ServerErrorException(BaseException):
    """_summary_: ServerErrorException
    _description_: The server error exception for thepeer sdk
    _usage_:
        raise ServerErrorException(errors)
    _example_:
        raise ServerErrorException({message: "We played a little bit too much and broke something"})
    """

    def __init__(self, errors):
        super().__init__(errors)

class ServiceUnavailableException(BaseException):
    """_summary_: ServiceUnavailableException
    _description_: The service unavailable exception for thepeer sdk
    _usage_:
        raise ServiceUnavailableException(errors)
    _example_:
        raise ServiceUnavailableException({message: "apparently our servers are taking a little vacation of reality"})
    """

    def __init__(self, errors):
        super().__init__(errors)

class UnauthorizedException(BaseException):
    """_summary_: UnauthorizedException
    _description_: The unauthorized exception for thepeer sdk
    _usage_:
        raise UnauthorizedException(errors)
    _example_:
        raise UnauthorizedException({message: "who are you?"})
    """

    def __init__(self, errors):
        super().__init__(errors)

class UnprocessableEntityException(BaseException):
    """_summary_: UnprocessableEntityException
    _description_: The unprocessable entity exception for thepeer sdk
    _usage_:
        raise UnprocessableEntityException(errors)
    _example_:
        raise UnprocessableEntityException({message: "The given data was invalid.",
    "errors": {
        "name": [
            "The name field is required."
        ],
        "email": [
            "The email field is required."
        ],
        "identifier": [
            "The identifier field is required."
        ]
    }})
    """

    def __init__(self, errors):
        super().__init__(errors)