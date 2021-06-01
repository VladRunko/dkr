from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase
from django import test
from .models import Task

User = get_user_model

class URLTests(test.TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class TaskTest(TestCase):
    def setUp(self):
        Task.objects.create(title="zadacha1", task="task of zadacha 1")
        Task.objects.create(title="zadacha2", task="task of zadacha 2")

    def test_task(self):
        zadacha1 = Task.objects.get(title="zadacha1")
        zadacha2 = Task.objects.get(title="zadacha2")

class SignUPTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='qwerty228', email='usertest@eee.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='testuser', password='qwerty228')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='qwerty228')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='testuser', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

