import hashlib
import hmac
import json  # type: ignore

import httpx
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
        """helper method to validate the signature of the data received
        from thepeer's servers, it's usually used for validating webhook events
        coming from thepeer's servers
        Args:
            data (dict|Any): the payload to which the signature is applied
            signature (string): the signature to be validated

        Returns:
            _type_: boolean if the signature is valid or not
        """
        return (
            signature == hmac.new(self.secret.encode(), data.encode(), hashlib.sha1()).hexdigest()
        )

    def index_user(self, name, identifier, email):

        """this method helps identify the user on thepeer's servers in order to facilitate
        more usage of the SDK
        it is usually the first method called by the user

        Args:
            name (string): the name of the registered user
            identifier (string): the universal identifier of the registered user
            email (string): the email of the registered user

        Returns:
            dict: the json response from the server containing the user's id and
            other related information
        """
        try:

            data = {"name": name, "identifier": identifier, "email": email}
            # convert the data to json
            data = json.dumps(data)
            response = httpx.post(f"{self.url}/users", data=data, headers=dict(self.headers))
            return response.json()

        except Exception as e:
            raise SwitchErrorStates(e).switch()

    def view_user(self, reference):
        """this method helps view the user's information on thepeer's servers
        it is usually called after the user has indexed himself

        Args:
            reference (string): the reference of the indexed user

        Returns:
            dict: the json response from the server containing the user's id and
            other related information
        """
        try:
            response = httpx.get(f"{self.url}/users/{reference}", headers=dict(self.headers))
            return response.json()
        except Exception as e:
            raise SwitchErrorStates(e).switch()

    def update_user(self, reference, data):
        """this method helps update the user's information on thepeer's servers
        it is usually called after the user has indexed himself

        Args:
            reference (string): the reference of the indexed user
            data (dict): the data to be updated

        Returns:
            dict: the json response from the server containing the user's id and
            other related information
        """
        try:
            data = json.dumps(data)
            response = httpx.put(
                f"{self.url}/users/{reference}", data=data, headers=dict(self.headers)
            )
            return response.json()
        except Exception as e:
            raise SwitchErrorStates(e).switch()

    def delete_user(self, reference):
        """this method helps delete the indexed user info on thepeer's servers
        a user can always reindex himself

        Args:
            reference (string): the reference of the indexed user
        """
        try:
            response = httpx.delete(f"{self.url}/users/{reference}", headers=dict(self.headers))
            return response.json()
        except Exception as e:
            raise SwitchErrorStates(e).switch()


# test function
thepeer = ThePeerInit(config("PEER_SECRET_KEY"))
test = thepeer.index_user("Osagie Iyayi", "iyayiemmanuel1@gmail.com", "iyayiemmanuel1@gmail.com")
get = thepeer.delete_user("e09c7080-acd9-452d-b3e4-83902fc1368b")
print(test)
