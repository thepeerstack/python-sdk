import unittest
from thepeer import main  # type: ignore

thepeer_test_suites = main.ThepeerInit("pssk_test_vwww1yvvpymamtut26x5tvpx1znrcmeis2k0kvcmwzjax")


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
            thepeer_test_suites.view_user("3bbb0fbf-82fa-48a0-80eb-d2c0338fe7dd"),
            {
                "indexed_user": {
                    "name": "Osagie Iyayi",
                    "identifier": "iyayiemmanuel1@gmail.com",
                    "identifier_type": "email",
                    "email": "iyayiemmanuel1@gmail.com",
                    "reference": "3bbb0fbf-82fa-48a0-80eb-d2c0338fe7dd",
                    "created_at": "2022-04-30T21:30:29.000000Z",
                    "updated_at": "2022-05-04T07:37:45.000000Z",
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
                            "name": "Osagie Iyayi",
                            "identifier": "iyayiemmanuel1@gmail.com",
                            "identifier_type": "email",
                            "email": "iyayiemmanuel1@gmail.com",
                            "reference": "3bbb0fbf-82fa-48a0-80eb-d2c0338fe7dd",
                            "created_at": "2022-04-30T21:30:29.000000Z",
                            "updated_at": "2022-05-04T07:37:45.000000Z",
                        },
                        {
                            "name": "Osagie Iyayi",
                            "identifier": "iyayiemmanuel1@gmail.com",
                            "identifier_type": "email",
                            "email": "iyayiemmanuel1@gmail.com",
                            "reference": "d2cb0c2c-7bd4-40a0-9744-824fbce176b7",
                            "created_at": "2022-05-04T07:37:44.000000Z",
                            "updated_at": "2022-05-04T07:37:44.000000Z",
                        },
                    ],
                    "meta": {"page": 1, "total": 2, "pageCount": 1, "perPage": 15},
                }
            },
        )

    def test_user_links(self):
        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(
            thepeer_test_suites.get_user_links("3bbb0fbf-82fa-48a0-80eb-d2c0338fe7dd"),
            {"links": []},
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
                "message": "The given data was invalid.",
                "errors": {"amount": ["The amount must be at least 10000."]},
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

    def test_authorize_direct_charge(self):
        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(
            thepeer_test_suites.authorize_direct_charge(
                "3bbb0fbf-82fa-48a0-80eb-d2c0338fe7dd", "charge"
            ),
            {
                "message": "The given data was invalid.",
                "errors": {"event": ["The selected event is invalid."]},
            },
        )

    def test_transaction_detail(self):
        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(
            thepeer_test_suites.get_transaction_detail("3bbb0fbf-82fa-48a0-80eb-d2c0338fe7dd"),
            {"message": "transaction not found"},
        )

    def test_refund_transaction(self):
        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(
            thepeer_test_suites.refund_transaction(
                "3bbb0fbf-82fa-48a0-80eb-d2c0338fe7dd", "possibly fraudulent"
            ),
            {"message": "this feature is only available on live mode"},
        )
