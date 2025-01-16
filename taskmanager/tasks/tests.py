from rest_framework.test import APITestCase
from rest_framework import status
from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            completed=False,
            user=self.user,
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertFalse(self.task.completed)
        self.assertEqual(self.task.user.username, "testuser")

class TaskAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")

    def test_create_task(self):
        url = "/api/tasks/"
        data = {"title": "New Task", "description": "New Description", "completed": False}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Task")

    def test_get_tasks(self):
        Task.objects.create(title="Task 1", description="Description 1", completed=False, user=self.user)
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Task 1")