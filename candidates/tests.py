from django.test import TestCase, Client
from django.urls import reverse
import json
from rest_framework import status



client = Client()


class BaseAPIRequests():
       
    @staticmethod
    def create_item(url,value):
        response = client.post(
            url,
            data=json.dumps(value),
            content_type='application/json'
        )
        return response.status_code

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
        self.url='/roles/'

        self.valid_values = [
            {'name': 'nome'}]

        self.invalid_values = [{},
            {'name':None},
            {'invalid_property':'abc'}]

class RunAllTests(TestCase):
    
    def setUp(self):
        self.test_inputs=[]
        self.test_inputs.append(PartyTestInputs())
        self.test_inputs.append(RoleTestInputs())
        self.test_inputs.append(PictureTestInputs())

    def test_create_valid_items(self):
        for input in self.test_inputs:
            for valid_value in input.valid_values:
                response_status = BaseAPIRequests.create_item(input.url,valid_value)
                self.assertEqual(response_status,status.HTTP_201_CREATED)

    def test_create_invalid_items(self):
        for input in self.test_inputs:
            for invalid_value in input.invalid_values:
                response_status = BaseAPIRequests.create_item(input.url,invalid_value)
                self.assertEqual(response_status,status.HTTP_400_BAD_REQUEST)