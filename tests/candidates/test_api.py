import json

import pytest
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def valid_party():
    {
            'id':'1',
            'name': 'nome',
            'number': 4
    }


@pytest.fixture
def invalid_party():    
    return {}


@pytest.fixture
def invalid_party2():
    return {
        'id':'teste'
    }


@pytest.mark.skip
def test_create_valid_party(client, valid_party):
    response = client.post(
        '/parties/',
        data=json.dumps(valid_party),
        content_type='application/json'
    )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.skip
def test_create_invalid_party(client, invalid_party):
    response = client.post(
        '/parties/',
        data=json.dumps(invalid_party),
        content_type='application/json'
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
        