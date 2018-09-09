from django.test import TestCase
from rest_framework.test import APIClient

from django.contrib.auth.models import User
from django.urls import reverse
from unittest.mock import patch
import json
from rest_framework import status


class TestAPIClient():
    def __init__(self, user):
        self.user = user
        self.client = APIClient()

    def create_item(self, url, value):
        self.client.force_authenticate(self.user)       
        return self.client.post(
            url,
            value,
            format='json'
        )

class PartyTestInputs():
    def __init__(self):
        self.url='/parties/'

        self.valid_values = [{
            'name': 'nome',
            'number': 4          
        }]

        self.invalid_values=[{},
            {'number':'teste'},
            {'name':None},
            {'invalid_property':'abc'}]

class RoleTestInputs():    
    def __init__(self):
        self.url='/roles/'

        self.valid_values = [{'name': 'nome'}]

        self.invalid_values = [{},
            {'name':None},
            {'invalid_property':'abc'}]

class PictureTestInputs():    
    def __init__(self):
        self.url='/pictures/'

        self.valid_values = [
            {
                'name': 'nome',
                'url': 'http://website.com/image.png'
            }
        ]

        self.invalid_values = [{},
            {'name':None},
            {'invalid_property':'abc'}]

class RunAllTests(TestCase):
    
    def setUp(self):
        user = User(username='lauren', is_staff=True, is_superuser=True)
        user.set_password('pass')
        user.save()
        self.client = TestAPIClient(user)
        self.test_inputs=[]
        self.test_inputs.append(PartyTestInputs())
        self.test_inputs.append(RoleTestInputs())
        self.test_inputs.append(PictureTestInputs())

    def test_create_valid_items(self):
        for input in self.test_inputs:
            for valid_value in input.valid_values:
                response = self.client.create_item(input.url, valid_value)
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)
   
    def test_create_invalid_items(self):
        for input in self.test_inputs:
            for invalid_value in input.invalid_values:
                response = self.client.create_item(input.url, invalid_value)
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)