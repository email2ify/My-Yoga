from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class TestHome(TestCase):
    def test_get_frontpage(self):
        """
        get index.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/frontpage.html')


class TestAbout(TestCase):
    def test_get_about(self):
        """
        get about.
        """
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')


class TestContact(TestCase):
    def test_get_about(self):
        """
        get contact.
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/contact.html')