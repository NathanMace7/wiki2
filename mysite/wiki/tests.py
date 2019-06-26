from django.test import TestCase, Client
from .models import Page
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from django.utils import timezone
import datetime

#Tests page creation
class PageCreationTestCase(TestCase):
    #Sets up a temporary page
    def setUp(self):
        page = Page.objects.create(title="Page_A", content="This is Page A for Testing")
        page.save()

        page = Page.objects.create(title="Page_B", content="This is Page B for Testing")
        page.save()

    #Searches for content within Page A
    def test_hello_world_a(self):
        response = self.client.get('/wiki/Page_A/')
        self.assertContains(response, 'This is Page A for Testing')

    #Searches for content within Page B
    def test_hello_world_b(self):
        response = self.client.get('/wiki/Page_B/')
        self.assertContains(response, 'This is Page B for Testing')

    #Searches for content within a non existing page, or the Create Page page.
    def test_page_non_existant(self):
        response = self.client.get('/wiki/IAmFailing/')
        self.assertContains(response, 'As this page does not exist, would you like to create it?')

#Tests page loading
class PageLoadTestCase(TestCase):

    #Tests for content within the Index page
    def test_index_view(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertContains(response, 'Wiki Index')

    #Tests for the content within the Uploads page
    def test_upload_view(self):
        response = self.client.get(reverse('wiki:upload_page'))
        self.assertContains(response, 'Upload A File')

    #Tests for the content within the Login page
    def test_login_view(self):
        response = self.client.get('/wiki/accounts/login/')
        self.assertContains(response, 'Username:')

#Tests Login System
class LoginTestCase(TestCase):

    #Tests the creation of an account
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('TestUser', 'TestUser@gmail.com', 'testingpassword')

    #Logs in and out with the account
    def testLogin(self):
        self.client.login(username='TestUser', password='testingpassword')
        response = self.client.get(reverse('wiki:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Logout")

#Tests Page Editing
class EditPageTest(TestCase):
    
    #Creates a tempory page to edit
    def test_edit_me_later(self):
        page = Page.objects.create(title = "editing", content = "Im going to be changing soon")
        page.save()

    #Log in
    def setUp(self):
        self.user = User.objects.create_user('TestUser', 'TestUser@gmail.com', 'testingpassword')

    #Tests for content within the Edit page
    def test_edit_page(self):
        self.client.login(username='TestUser', password='testingpassword')
        response = self.client.post('/wiki/editing/edit', follow=True)
        self.assertContains(response, 'Editing')