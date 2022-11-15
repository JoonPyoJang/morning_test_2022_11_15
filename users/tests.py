from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.

class UserLoginAPITestCase(APITestCase):
    def test_registration(self):
        url = reverse("sign-up")
        user_data={
            "username" : "jjpyo1009",
            "password" : "123",
            "email" : "jjpyo1009@asd.asd",
            "fullname" : "jangjoonpyo",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.data, {'message': '가입 완료!!'})
