import ipdb
from django.db import IntegrityError
from django.forms import ValidationError
from django.test import TestCase
from model_bakery import baker
from users.models import User


class UserModelTest(TestCase):
    def test_keys_of_abstract_user(self):
        user = baker.make("users.User")
        expected_keys = {
            "is_superuser",
            "is_staff",
            "is_active",
            "first_name",
            "email",
            "last_name",
            "id",
            "date_joined",
            "username",
            "_state",
            "department_id",
            "last_login",
            "password",
        }
        received_keys = set(vars(user).keys())

        self.assertSetEqual(expected_keys, received_keys)

    def test_creation_of_a_user(self):
        user = baker.make("users.User")

        self.assertIn("id", vars(user))
        self.assertIn("username", vars(user))
        self.assertIn("password", vars(user))
        self.assertIn("department_id", vars(user))
        self.assertIsNone(user.department_id)

    def test_unique_username(self):
        user = baker.make("users.User")

        with self.assertRaises(IntegrityError):
            baker.make("users.User", username=user.username)
