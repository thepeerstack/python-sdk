from .exceptions import ForbiddenException  # type: ignore
from .exceptions import NotAcceptableException  # type: ignore
from .exceptions import NotFoundException  # type: ignore
from .exceptions import ServerErrorException  # type: ignore
from .exceptions import ServiceUnavailableException  # type: ignore
from .exceptions import UnauthorizedException  # type: ignore
from .exceptions import UnprocessableEntityException  # type: ignore


class SwitchErrorStates:
    """_summary_
    A class for switching between various error status codes returned from the peer servers
    """

    def __init__(self, error):
        self.errordata = error.response.data.error

    def switch(self):
        status = self.error.response.status
        error_message = self.error.response.data.message
        if status == 401:
            raise UnauthorizedException({"message": error_message})
        elif status == 403:
            raise ForbiddenException({"message": error_message})
        elif status == 404:
            raise NotFoundException({"message": error_message})
        elif status == 406:
            raise NotAcceptableException({"message": error_message})
        elif status == 422:
            raise UnprocessableEntityException({"message": error_message})
        elif status == 500:
            raise ServerErrorException({"message": error_message})
        elif status == 503:
            raise ServiceUnavailableException({"message": error_message})
