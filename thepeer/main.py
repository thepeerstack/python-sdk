import requests
import httpx
import hmac
import hashlib
from decouple import config  # type: ignore
from utils.constants import BASE_URL  # type: ignore
from utils.exceptions.handleErrors import SwitchErrorStates  # type: ignore


class ThePeerInit:
    def __init__(self, secret):
        # pass a default value for the url
        self.url = BASE_URL
        self.secret = secret
        # set default headers to be used in all requests
        self.headers = {"x-api-key": self.secret, "content-Type": "application/json"}

    def validate_signature(self, data, signature):
        """helper method to validate the signature of the data received from thepeer's servers
        Args:
            data (dict|Any): the payload to which the signature is applied
            signature (string): the signature to be validated

        Returns:
            _type_: boolean if the signature is valid or not
        """
        return (
            signature
            == hmac.new(self.secret.encode(), data.encode(), hashlib.sha1()).hexdigest()
        )

    def index_user(self, name, identifier, email):
        try:
            """this method helps identify the user on thepeer's servers in order to facilitate more usage of the SDK
            it is usually the first method called by the user

            Args:
                name (string): the name of the registered user
                identifier (string): the universal identifier of the registered user
                email (string): the email of the registered user

            Returns:
                dict: the json response from the server containing the user's id and other related information
            """
            data = {"name": name, "identifier": identifier, "email": email}
            response = httpx.post(
                f"{self.url}/users", data=data, headers=dict(self.headers)
            )
            return response.json()

        except Exception as e:
            raise SwitchErrorStates(e).switch()


# test function
thepeer = ThePeerInit(config("PEER_SECRET_KEY"))
test = thepeer.index_user("Osagie Iyayi", "Ewave", "iyayiemmanuel1@gmail.com")
print(test)
