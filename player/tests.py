from django.test import TestCase
from .models import Player, GenericAvatar
import json


class CreateUserTest(TestCase):
    def setUp(self):
        self.avatar = GenericAvatar.objects.create()

    def test_create_via_API(self):
        url = '/player/api/create/'
        data = {'sex': 'female'}
        response = self.client.post(url, json.dumps(data), content_type='application/json', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['is_host'], False)
