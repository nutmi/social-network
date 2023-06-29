import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import GroupRoom, NormalRoom
from .serializers import NormalRoomSerializer


class ModelTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="user1")
        self.user2 = User.objects.create(username="user2")

    def test_create_group_room(self):
        group_room = GroupRoom.objects.create(creator=self.user1)
        self.assertEqual(group_room.creator, self.user1)
    
    def test_create_normal_room(self):
        normal_room = NormalRoom.objects.create(user_1=self.user1, user_2=self.user2)
        self.assertEqual(normal_room.user_1, self.user1)
        self.assertEqual(normal_room.user_2, self.user2)

class ViewSetTest(TestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create(username="user1")
        self.user2 = User.objects.create(username="user2")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user1)
    
    def test_create_normal_room(self):
        url = '/normalroom/'
        data = {'user_1': self.user1.id, 'user_2': self.user2.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['user_1'], self.user1.id)
        self.assertEqual(response.data['user_2'], self.user2.id)


