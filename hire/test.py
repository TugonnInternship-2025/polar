from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import HireModel


class CreateHireTest(TestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(
            username="Johnny bravo",
            password="notAPassword-123",
            email="johnny@test.com"
        )
        self.talent_user = User.objects.create_user(
            username="Ademola Micheal",
            password="notAPassword-123",
            email="demola@test.com"
        )
        self.client = Client()
        
        self.client.login(
            username="Johnny bravo",
            password="notAPassword-123",
        )
        
    def test_create_hire(self):
        url = reverse("hire:create-hire",args=[self.talent_user.id])
        response = self.client.post(url)
        
        self.assertEqual(response.status_code,201)
        self.assertEqual(HireModel.objects.count(),1)
        
        hire = HireModel.objects.first()
        self.assertEqual(hire.client, self.client_user)
        self.assertEqual(hire.talent, self.talent_user)
        self.assertEqual(hire.status, HireModel.STATUS_PENDING)