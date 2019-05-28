import datetime

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
from .models import Page

class PageCreationTestCase(TestCase):
    def setUp(self):
        page = Page.objects.create(title="Page_A", content="This is Page A for Testing")
        page.save()

        page = Page.objects.create(title="Page_B", content="This is Page B for Testing")
        page.save()

    def test_hello_world_a(self):
        response = self.client.get('/wiki/Page_A/')
        self.assertContains(response, 'This is Page A for Testing')

    def test_hello_world_b(self):
        response = self.client.get('/wiki/Page_B/')
        self.assertContains(response, 'This is Page B for Testing')

    def test_page_non_existant(self):
        response = self.client.get('/wiki/IAmFailing/')
        self.assertContains(response, 'As this page does not exist, would you like to create it?')

class PageLoadTestCase(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertContains(response, 'Wiki Index')

    def test_upload_view(self):
        response = self.client.get(reverse('wiki:upload_page'))
        self.assertContains(response, 'Upload A File')

    def test_login_view(self):
        response = self.client.get('/wiki/accounts/login/')
        self.assertContains(response, 'Username:')

class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('TestUser', 'TestUser@gmail.com', 'testingpassword')

    def testLogin(self):
        self.client.login(username='TestUser', password='testingpassword')
        response = self.client.get(reverse('wiki:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Logout")

class EditPageTest(TestCase):
    def test_edit_me_later(self):
        page = Page.objects.create(title = "editing", content = "Im going to be changing soon")
        page.save()

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('TestUser', 'TestUser@gmail.com', 'testingpassword')

    def test_edit_page(self):
        self.client.login(username='TestUser', password='testingpassword')
        response = self.client.post('/wiki/editing/edit', follow=True)
        self.assertContains(response, 'Editing')