from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class RegisterTestCase(APITestCase):
    
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.data = {'username': 'mike', 'first_name': 'Mike', 'last_name': 'Tyson'}
    
    def test_register(self):
        # data = {
        #     "username": "testcase",
        #     "email": "testcase@example.com",
        #     "password": "testcase3687",
        #     "password2": "testcase3687",
        # }
        response = self.client.post(reverse('register'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
class LoginLogout(APITestCase):
    
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.data = {'username': 'mike', 'first_name': 'Mike', 'last_name': 'Tyson'}
        
    def test_login(self):
        data = {
            "username": "john",
            "password": "johnpassword"
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    # def test_logout(self):
    #     self.token = Token.objects.get(user__username="john")
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    #     response = self.client.post(reverse('logout'))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)