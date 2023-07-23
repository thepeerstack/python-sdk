import unittest
from thepeer import Thepeer  # type: ignore

thepeer_test_suites = Thepeer("pssk_test_vwww1yvvpymamtut26x5tvpx1znrcmeis2k0kvcmwzjax")


class ThePeerInitMethods(unittest.TestCase):
    def test_validate_signature(self):
        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(
            thepeer_test_suites.validate_signature(
                "I love the peer", "27154e4751dc49d1b40281b18deecd4fd2392e43"
            ),
            True,
        )

    def test_index_user(self):
        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(
            thepeer_test_suites.index_user(
                "Osagie Iyayi", "iyayiemmanuel1@gmail.com", "iyayiemmanuel1@gmail.com"
            ),
            {"message": "identifier exists"},
        )

    def test_view_user(self):
        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(
            thepeer_test_suites.view_user("d2cb0c2c-7bd4-40a0-9744-824fbce176b7"),
            {
                "indexed_user": {
                    "reference": "d2cb0c2c-7bd4-40a0-9744-824fbce176b7",
                    "name": "Osagie Iyayi",
                    "identifier": "iyayiemmanuel1@gmail.com",
                    "identifier_type": "email",
                    "email": "iyayiemmanuel1@gmail.com",
                    "created_at": "2022-05-04T07:37:44.000000Z",
                    "updated_at": "2022-05-04T07:37:44.000000Z",
                }
            },
        )

    def test_all_users(self):
        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(
            thepeer_test_suites.all_users(),
            {
                "indexed_users": {
                    "data": [
                        {
                            "reference": "5c4961bf-56ca-4a28-80af-214543cdf382",
                            "name": "Adesubomi Jaiyeola",
                            "identifier": "08095743249",
                            "identifier_type": "email",
                            "email": "subomi.ja@gmail.com",
                            "created_at": "2023-04-04T14:49:30.000000Z",
                            "updated_at": "2023-04-04T14:49:30.000000Z",
                        },
                        {
                            "reference": "d2cb0c2c-7bd4-40a0-9744-824fbce176b7",
                            "name": "Osagie Iyayi",
                            "identifier": "iyayiemmanuel1@gmail.com",
                            "identifier_type": "email",
                            "email": "iyayiemmanuel1@gmail.com",
                            "created_at": "2022-05-04T07:37:44.000000Z",
                            "updated_at": "2022-05-04T07:37:44.000000Z",
                        },
                        {
                            "reference": "e9d09152-fb47-4bb7-a162-7a326cd35c32",
                            "name": "Jenni Madu",
                            "identifier": "jennifermadu903@gmail.com",
                            "identifier_type": "email",
                            "email": "jennifermadu903@gmail.com",
                            "created_at": "2023-04-13T14:04:32.000000Z",
                            "updated_at": "2023-04-13T14:04:32.000000Z",
                        },
                    ]
                },
                "meta": {"page": 1, "total": 3, "pageCount": 1, "perPage": 15},
            },
        )

    def test_user_links(self):
        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(
            thepeer_test_suites.get_user_links("d2cb0c2c-7bd4-40a0-9744-824fbce176b7"),
            {"links": None},
        )

    def test_single_link(self):
        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(
            thepeer_test_suites.get_single_link("3bbb0fbf-82fa-48a0-80eb-d2c0338fe7dd"),
            {"message": "link not found"},
        )

    def test_charge_link(self):
        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(
            thepeer_test_suites.charge_link(
                "3bbb0fbf-82fa-48a0-80eb-d2c0338fe7dd", 2000, "try thepeer"
            ),
            {
                "errors": {
                    "amount": ["The amount field must be numeric value between 10000 and 100000000"]
                },
                "message": "The given data was invalid",
            },
        )

    def test_charge_link_2(self):
        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(
            thepeer_test_suites.charge_link(
                "3bbb0fbf-82fa-48a0-80eb-d2c0338fe7dd", 10000, "try thepeer"
            ),
            {"message": "link not found"},
        )

    def test_authorize_charge(self):
        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(
            thepeer_test_suites.authorize_charge("3bbb0fbf-82fa-48a0-80eb-d2c0338fe7dd", "success"),
            {"message": "resource not found"},
        )

    def test_transaction_detail(self):
        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(
            thepeer_test_suites.get_transaction_detail("d761e113-1e6d-456d-8341-79a963234511"),
            {
                "transaction": {
                    "id": "d761e113-1e6d-456d-8341-79a963234511",
                    "amount": 1000000,
                    "channel": "checkout",
                    "refund": False,
                    "checkout": {
                        "id": "402bc104-b17e-4046-bef5-4e3df34aac5c",
                        "amount": 1000000,
                        "email": "iyayiemmanuel1@gmail.com",
                        "currency": "NGN",
                        "status": "paid",
                        "linked_account": {
                            "user": {
                                "name": "Trojan Okoh",
                                "identifier": "trojan",
                                "identifier_type": "username",
                            },
                            "business": {
                                "name": "Cash App",
                                "logo": "https://palaciodepeer.s3.us-east-2.amazonaws.com/business_logos/UJimBqYOu7KQIM3DwCWOuKjkDbBbVLYRuYRTgxKh.png",  # noqa: E501
                                "logo_colour": "#77cc33",
                            },
                        },
                        "meta": {},
                        "updated_at": "2023-07-22T23:55:21.000000Z",
                        "created_at": "2023-07-22T23:48:15.000000Z",
                    },
                    "user": {
                        "reference": "2992e5b4-acb7-49b4-848d-f5a7ca225413",
                        "name": "Checkout",
                        "identifier": "checkout",
                        "identifier_type": "email",
                        "email": "iyayiemmanuel1@gmail.com",
                        "created_at": "2023-07-22T23:55:19.000000Z",
                        "updated_at": "2023-07-22T23:55:19.000000Z",
                    },
                    "charge": 10000,
                    "currency": "NGN",
                    "mode": "credit",
                    "reference": "c3f0a7b1ec0dbb3242eeaea7f380e96e",
                    "remark": "checkout",
                    "status": "success",
                    "type": "peer",
                    "meta": None,
                    "peer": {
                        "business": {
                            "name": "Cash App",
                            "logo": "https://palaciodepeer.s3.us-east-2.amazonaws.com/business_logos/UJimBqYOu7KQIM3DwCWOuKjkDbBbVLYRuYRTgxKh.png",  # noqa: E501
                            "logo_colour": "#77cc33",
                        },
                        "user": {
                            "name": "Trojan Okoh",
                            "identifier": "trojan",
                            "identifier_type": "username",
                        },
                    },
                    "updated_at": "2023-07-22T23:55:20.000000Z",
                    "created_at": "2023-07-22T23:55:20.000000Z",
                }
            },
        )

    def test_refund_transaction(self):
        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(
            thepeer_test_suites.refund_transaction(
                "d761e113-1e6d-456d-8341-79a963234511", "possibly fraudulent"
            ),
            {"message": "transactions can only be refunded on live mode"},
        )
