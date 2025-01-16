from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class AccountAPITest(APITestCase):
    def test_register_user(self):
        url = "/api/users/"
        data = {"username": "newuser", "password": "newpassword"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["username"], "newuser")

    def test_get_user_list(self):
        User.objects.create_user(username="testuser1", password="password1")
        User.objects.create_user(username="testuser2", password="password2")
        self.client.login(username="testuser1", password="password1")

        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_user_login(self):
        User.objects.create_user(username="loginuser", password="password123")
        url = "/api/token/"
        data = {"username": "loginuser", "password": "password123"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
