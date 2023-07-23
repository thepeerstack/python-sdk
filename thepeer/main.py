import hmac
import hashlib
import json  # type: ignore

import httpx  # noqa: E402
from .utils.constants import BASE_URL  # noqa: E402
from .utils.exceptions.handleErrors import SwitchErrorStates  # noqa: E402
from typing import Union


class Thepeer:
    def __init__(self, secret: str):
        # pass a default value for the url
        self.url = BASE_URL
        self.secret = secret
        # set default headers to be used in all requests
        self.headers = {"x-api-key": self.secret, "content-Type": "application/json"}

    def get_businesses(self, channel: str):
        """This endpoint returns businesses based on the API they integrated.
        Args:
            channel (string): The specific API to return businesses of.
            Supported values are `send`, `checkout`, and `direct_charge`.
        """
        try:
            response = httpx.get(
                f"{self.url}/businesses?channel={channel}", headers=dict(self.headers)
            )
            return response.json()
        except Exception as e:
            raise SwitchErrorStates(e).switch()

    def generate_checkout(self, data: dict[str, Union[str, int]]):
        """
        This is a checkout endpoint that you can use to generate a link for your customer to make a
        one-time payment with.
        Args:
            data (dict): The request payload which contains the `currency` (NGN),
            `amount`, `email`, and optionally `redirect_url` and `meta` fields.
        """
        try:
            parsed_data = json.dumps(data)
            response = httpx.post(
                f"{self.url}/checkout", data=parsed_data, headers=dict(self.headers)
            )
            return response.json()
        except Exception as e:
            raise SwitchErrorStates(e).switch()

    def validate_signature(self, data, signature: str):
        """helper method to validate the signature of the data received
        from thepeer's servers, it's usually used for validating webhook events
        coming from thepeer's servers
        Args:
            data (dict|Any): the payload to which the signature is applied
            signature (string): the signature to be validated

        Returns:
            _type_: boolean if the signature is valid or not
        """
        SHA1 = hashlib.sha1
        return signature == hmac.new(self.secret.encode(), data.encode(), SHA1).hexdigest()

    def index_user(self, name: str, identifier: str, email: str):

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
            parsed_data = json.dumps(data)
            response = httpx.post(f"{self.url}/users", data=parsed_data, headers=dict(self.headers))
            return response.json()

        except Exception as e:
            raise SwitchErrorStates(e).switch()

    def view_user(self, reference: str):
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

    def all_users(self, page=1, per_page=15):
        """this method gets all the indexed users of a business

        Args:
            page (int): a specific page of pagination instances
            per_page (int): number of users to display in a single paginated instance page

        Returns:
            dict: a dict containing paginated lists of dicts of indexed users
        """

        try:
            response = httpx.get(
                f"{self.url}/users?page={page}&perPage={per_page}", headers=dict(self.headers)
            )
            return response.json()
        except Exception as e:
            raise SwitchErrorStates(e).switch()

    def update_user(self, reference: str, **data):
        """this method helps update the user's information on thepeer's servers
        it is usually called after the user has indexed himself

        Args:
            reference (string): the reference of the indexed user
            data (dict): the data to be updated which is a dictionary
            of at least one of the fields (name, identifier, identifier_type,email)

        Returns:
            dict: the json response from the server containing the user's id and
            other related information
        """
        try:
            parsed_data = json.dumps(data)
            response = httpx.put(
                f"{self.url}/users/{reference}", data=parsed_data, headers=dict(self.headers)
            )
            return response.json()
        except Exception as e:
            raise SwitchErrorStates(e).switch()

    def delete_user(self, reference: str):
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

    def get_user_links(self, reference: str):
        """This endpoint returns all linked accounts of a user, the user's account details,
          as well as the business the account is on.


        Args:
            reference (string): the reference of the indexed user

        Returns:
            dict: the json response from the server containing the linked accounts
            related to the user's id and other related information
        """
        try:
            response = httpx.get(f"{self.url}/users/{reference}/links", headers=dict(self.headers))
            return response.json()
        except Exception as e:
            raise SwitchErrorStates(e).switch()

    def get_single_link(self, link_id: str):
        """This endpoint returns a user's linked account's details.


        Args:
            link_id (string): the link ID

        Returns:
            dict: the json response from the server containing the payment link id and
            other related information
        """
        try:
            response = httpx.get(f"{self.url}/link/{link_id}", headers=dict(self.headers))
            return response.json()
        except Exception as e:
            raise SwitchErrorStates(e).switch()

    def charge_link(self, link_id: str, amount: Union[str, int], remark: str, currency="NGN"):
        """allows a business to charge a user via their linked account

        Args:
            link_id (string):the link ID
            data (dict): the request payload which contains the amount and remark and optionally,
            a currency (which could be NGN or USD default being NGN)

        Returns:
            dict: a transaction object generated from a webhook. more info about a
            transaction object here https://docs.thepeer.co/transaction/transaction-object
        """
        try:
            data = json.dumps({"amount": amount, "remark": remark, "currency": currency})
            response = httpx.post(
                f"{self.url}/link/{link_id}/charge", data=data, headers=dict(self.headers)
            )
            return response.json()
        except Exception as e:
            raise SwitchErrorStates(e).switch()

    def authorize_charge(self, charge_reference: str, event: str):
        """allows a business to authorize a direct charge request made by a user

        Args:
            charge_reference (string): reference generated from the direct charge webhook event
            event (string): a string which contains the kind of webhook event

        Returns:
            dict: containing a key value pair of the event(key) and the type of event
        """
        try:
            data = json.dumps({"event": event})
            response = httpx.post(
                f"{self.url}/authorization/{charge_reference}",
                data=data,
                headers=dict(self.headers),
            )
            return response.json()

        except Exception as e:
            raise SwitchErrorStates(e).switch()

    def get_transaction_detail(self, transaction_id: str):
        """Get the details about a transaction
        Args:
            transaction_id (string): the unique identifier of the transaction

        Returns:
            dict:containing the transaction object. more about a transaction object here
            https://docs.thepeer.co/transaction/transaction-object#anatomy-of-a-transaction-object
        """
        try:
            response = httpx.get(
                f"{self.url}/transactions/{transaction_id}", headers=dict(self.headers)
            )
            return response.json()
        except Exception as e:
            raise SwitchErrorStates(e).switch()

    def refund_transaction(self, transaction_id: str, reason: str):

        """This method allows a business to refund a transaction back to the user
        who made the transaction for obvious reasons.

        Args:
            transaction_id (string): the unique identifier of the transaction
            reason (string): a string explaining the reason for the refund

        Returns:
             dict:
             containing the transaction object. more about a transaction object can be found here
             https://docs.thepeer.co/transaction/transaction-object#anatomy-of-a-transaction-object
        """
        try:
            data = json.dumps({"reason": reason})
            response = httpx.post(
                f"{self.url}/transactions/{transaction_id}/refund",
                data=data,
                headers=dict(self.headers),
            )
            return response.json()
        except Exception as e:
            raise SwitchErrorStates(e).switch()
