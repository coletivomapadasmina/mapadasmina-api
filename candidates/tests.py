from django.test import TestCase, Client
client = Client()
class CreatePartyTest(TestCase):
    """ Test module for inserting a new party """
    
    def setUp(self):
        self.valid_party = {
            'id':'1',
            'name': 'nome',
            'number': 4
        }
        self.invalid_party1 = {
            
        }
        self.invalid_party2 = {
            'id':'teste'
        }

    def test_create_valid_party(self):
        response = client.post(
            reverse('parties'),
            data=json.dumps(self.valid_party),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_invalid_party(self):
        response = client.post(
            reverse('parties'),
            data=json.dumps(self.invalid1_party),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        