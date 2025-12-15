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

class UpdateHireStatusTest(TestCase):
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
        self.hire = HireModel.objects.create(
            client = self.client_user,
            talent = self.talent_user,
            talent_name=self.talent_user.username,
            talent_email=self.talent_user.email,
            status=HireModel.STATUS_PENDING
        )
        self.url = reverse("hire:update-status", args=[self.hire.id])
        self.client = Client()

    def test_client_can_mark_as_completed(self):
        self.client.login(username="Johnny bravo", password="notAPassword-123")
        response = self.client.post(f"{self.url}?status={HireModel.STATUS_COMPLETED}")
        
        self.hire.refresh_from_db()
        self.assertEqual(response.status_code,200)
        self.assertEqual(self.hire.status, HireModel.STATUS_COMPLETED)
        
    def test_talent_cannot_mark_completed(self):
        self.client.login(username="Ademola Micheal", password="notAPassword-123",)
        
        response = self.client.post(f"{self.url}?status={HireModel.STATUS_COMPLETED}")
        
        self.hire.refresh_from_db()
        self.assertEqual(response.status_code,403)
        self.assertEqual(self.hire.status, HireModel.STATUS_PENDING)
        
    def test_cannot_transition_from_cancelled_to_completed(self):
        self.hire.status = HireModel.STATUS_CANCELLED
        self.hire.save()
        self.client.login(username="Johnny bravo", password="notAPassword-123")
        
        response = self.client.post(f"{self.url}?status={HireModel.STATUS_COMPLETED}")
        
        self.hire.refresh_from_db()
        self.assertEqual(response.status_code,400)
        self.assertEqual(self.hire.status, HireModel.STATUS_CANCELLED)