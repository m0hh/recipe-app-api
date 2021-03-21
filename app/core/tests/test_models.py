from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        # test create user
        email = 'test@london.com'
        password = 'testing321'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = "test@LONDONAPPDEV.COM"
        user = get_user_model().objects.create_user(email, 'test321')

        self.assertEqual(user.email , email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test321")
    
    def test_create_new_superUser(self):
        user = get_user_model().objects.create_superuser(
            'test@london.com',
            'test321'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

        