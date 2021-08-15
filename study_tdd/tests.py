from django.test import TestCase
from django.urls import resolve
from django.http import HttpResponse
from .views import *


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page_returns_correct_html(self):
        request = HttpResponse()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.strip().startswith('<!DOCTYPE html>'))
        self.assertIn('<title>To-Do</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))