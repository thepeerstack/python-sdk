from .base import BaseException as error


class UnprocessableEntityException(error):
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
