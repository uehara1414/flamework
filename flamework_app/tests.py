from django.test import TestCase
from .models import UserInfo


class Test(TestCase):

    def test_zipcode(self):
        userinfo1 = UserInfo(zipcode='2140005')
        userinfo2 = UserInfo(zipcode='2140004')

        self.assertEqual(userinfo1.get_zip_distance(userinfo2.zipcode), 1)

        self.assertEqual(userinfo1.get_zip_distance('2140033'), 2)

        self.assertEqual(userinfo1.get_zip_distance('2140105'), 3)

        self.assertEqual(userinfo1.get_zip_distance('2140005'), 0)
