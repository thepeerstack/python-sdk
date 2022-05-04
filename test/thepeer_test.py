import unittest

from thepeer.main import ThePeerInit


thepeer_test_suites = ThePeerInit("pssk_test_vwww1yvvpymamtut26x5tvpx1znrcmeis2k0kvcmwzjax")


class ThePeerInitMethods(unittest.TestCase):
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
        self.assertEqual(
            thepeer_test_suites.get_user_links("3bbb0fbf-82fa-48a0-80eb-d2c0338fe7dd"),
            {"links": []},
        )

    def test_single_link(self):
        self.assertEqual(
            thepeer_test_suites.get_single_link("3bbb0fbf-82fa-48a0-80eb-d2c0338fe7dd"),
            {"message": "link not found"},
        )
