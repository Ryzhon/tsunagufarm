from django.test import TestCase
from user.models import User

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email="test@example.com", name="testuser")
        self.assertEqual(user.email, "test@example.com")