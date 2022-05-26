# thepeer python-sdk

![example workflow](https://github.com/thepeerstack/python-sdk/actions/workflows/pytests.yml/badge.svg) ![PyPI - Downloads](https://img.shields.io/pypi/dm/pythepeer?style=flat-square) ![PyPI - License](https://img.shields.io/pypi/l/pythepeer) ![PyPI](https://img.shields.io/pypi/v/pythepeer) ![Codecov](https://img.shields.io/codecov/c/gh/E-wave112/py-thepeer?token=gYijsI9TCm)

> Thepeer's official python sdk for developers to use in their python projects.

- To start using this sdk, create an account at https://thepeer.co/ if you haven't already.
- You can then retrieve your API keys from your [dashboard](https://dashboard.thepeer.co/)

## Installation
To install this sdk, run the command:
```bash
pip install pythepeer
```

## Usage
Instantiate the ThepeerInit class like so:
```python
import thepeer
from thepeer.main import ThepeerInit

# create an instance of ThepeerInit class

thepeer_instance = ThepeerInit("YOUR_API_KEY_HERE")

```

## Available methods exposed by the sdk

**Note:**
 - For more info about the exposed methods, please refer to the general [documentation](https://docs.thepeer.co/)
 - Be sure to keep your API Credentials securely in [environment variables](https://www.twilio.com/blog/environment-variables-python)
### Indexing a user
This describes how to index a user on your account (this is usually the first step before using other methods)

```python
test = thepeer_instance.index_user("Osagie Iyayi", "iyayiemmanuel1@gmail.com", "iyayiemmanuel1@gmail.com")
```

#### Parameters supported

| Parameters           | Data type                 | Required | Description                                                                                                                                                                                                                                         |
|----------------------|---------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```name```        | ```string```                   | ```true```     | ```The name of user to be indexed```.
| ```identifier```            | ```string```                   |  ```true```    | ```the identifier of the account(either email or username).```
| ```email```        | ```string```                   | ```true```     | ```the email of the user```                                                                        |

### Validating a HMAC signature
This method validates incoming an [hmac](https://www.okta.com/identity-101/hmac/) signature with the payload and credentials that was passed with it

**Pro Tip:** it is used to verify that an incoming webhook event/response is coming from thepeer's servers

```python
test = thepeer_instance.validate_signature(data,signature)
```
#### Parameters supported

| Parameters           | Data type                 | Required | Description                                                                                                                                                                                                                                         |
|----------------------|---------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```data```           | ```dictionary```                  |  ```true```    | ```the payload containing the data to be authenticated```
|  ```signature```       | ```string```                   | ```true```     | ```The HMAC signature```                                                                        |

### Get an indexed user
This method gets the information of an indexed user

```python
test = thepeer_instance.view_user("3bbb0fbf-82fa-48a0-80eb-d2c0338fe7dd")
```

#### Parameters supported


| Parameters           | Data type                 | Required | Description                                                                                                                                                                                                                                         |
|----------------------|---------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```reference```            | ```string```                  |  ```true```    | ```the unique reference returned when the user was indexed```

### Get all indexed users
This method returns all indexed users for a specific account

```python
test = thepeer_instance.all_users(1,15)
```

#### Parameters supported

| Parameters           | Data type                 | Required | Description                                                                                                                                                                                                                                         |
|----------------------|---------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```page```            | ```integer```               |  ```false```    | ```the first page displaying all the indexed users. defaults to 1```
|  ```per_page```      | ```integer```                  | ```false```     | ```The number of users to display per page. defaults to 15          ```                                                          |


### Update an indexed user
This methods helps to update the details of an indexed user

```python
test = thepeer_instance.update_user(reference,**data)
```
#### Parameters supported

| Parameters           | Data type                 | Required | Description                                                                                                                                                                                                                                         |
|----------------------|---------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```reference```            | ```string```               |  ```true```    | ```the unique reference returned when the user was indexed```
|  ```data```      | ```Any```                  | ```true```    | ```A keyword argument which contains on or more of the indexed user's email, name or identifier```                                                                   |

### Sample
```python
test = thepeer_instance.update_user("3bbb0fbf-82fa-48a0-80eb-d2c0338fe7dd", identifier="dwave101@yahoo.com",
    name="Edmond Kirsch",
    email="dwave101@gmail.com")
```
### Remove an indexed user
This methods helps to remove the details of an indexed user from a specific account

```python
test = thepeer_instance.delete_user("3bbb0fbf-82fa-48a0-80eb-d2c0338fe7dd")
```

#### Parameters supported

| Parameters           | Data type                 | Required | Description                                                                                                                                                                                                                                         |
|----------------------|---------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```reference```            | ```string```                  |  ```true```    | ```the unique reference returned when the user was indexed```

### Get user links

This method gets all payment links associated to an indexed user
```python
test = thepeer_instance.get_user_links("3bbb0fbf-82fa-48a0-80eb-d2c0338fe7dd")
```
#### Parameters required

| Parameters           | Data type                 | Required | Description                                                                                                                                                                                                                                         |
|----------------------|---------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```reference```            | ```string```                  |  ```true```    | ```the unique reference returned when the user was indexed```


### Get single link

This method gets the payment information located in a payment link

```python
test = thepeer_instance.get_single_link("da14a90c-61c2-4cf7-a837-e3112a2d0c3d")
```

#### Parameters required

| Parameters           | Data type                 | Required | Description                                                                                                                                                                                                                                         |
|----------------------|---------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```link_id```           | ```string```                  |  ```true```    | ```the unique link_id containing the payment information```


### Charge a link
This method allows a business to charge a user via their linked account
```python
test = thepeer_instance.charge_link(link_id, amount, remark, currency)
```

#### Parameters required

| Parameters           | Data type                 | Required | Description                                                                                                                                                                                                                                         |
|----------------------|---------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```link_id```        | ```string```                   | ```true```     | ```the unique link_id containing the payment information```
| ```amount```            | ```integer```               |  ```true```    | ```the amount of the whole transaction```
| ```remark```        | ```string```                   | ```true```     | ```short detail about the transaction```                                                                     |
| ```currency```               | ```string```                    | ```false```    | ```The denomination medium of paying (either one of NGN and USD). defaults to NGN```

### Authorize charge
This method allows a business to authorize a direct charge request made by a user

```python
test = thepeer_instance.authorize_charge(charge_reference, event)
```
#### Parameters required

| Parameters           | Data type                 | Required | Description                                                                                                                                                                                                                                         |
|----------------------|---------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```charge_reference```            | ```string```          |  ```true```   | ```the reference associated to a pending charge request```
|  ```event```     | ```string```                | ```true```     | ```the type of webhook event```                                              |

**Pro Tip:** the various types of webhook events are available [here](https://docs.thepeer.co/authorization/process-authorization-requests#supported-events)


### Get transaction detail
This method gets the details of a transaction
```python
test = thepeer_instance.get_transaction_detail("eda58ee3-4f2c-4aa4-9da7-10a2b8ced453")
```

#### Parameters required

| Parameters           | Data type                 | Required | Description                                                                                                                                                                                                                                         |
|----------------------|---------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```transaction_id```           | ```string```                  |  ```true```    | ```the unique transaction identifier```

### Refund transaction
This method allows a business to refund a transaction back to the user for obvious reasons
```python
test = thepeer_instance.refund_transaction("28e52edf-16d9-4921-8a54-ef34d7029707", "possible threat actor"):
```

#### Parameters required
| Parameters           | Data type                 | Required | Description                                                                                                                                                                                                                                         |
|----------------------|---------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```transaction_id```            | ```string```          |  ```true```   | ```the unique transaction identifier```
|  ```reason```     | ```string```                | ```false```    | ```a short sentence explaining reasons for the refund```                                              |



 <!-- ## License
This project is MIT Licensed (MIT). Please see the [License File](https://github.com/thepeerstack/python-sdk/blob/main/LICENSE) for more information. -->
