from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        html = response.content.decode('utf8') #3
        self.assertTrue(html.startswith('<html>')) #4
        self.assertIn('<title>To-Do lists</title>', html) #5
        self.assertTrue(html.endswith('</html>')) #4
        
        self.assertTemplateUsed(response, 'home.html')        

# Create your tests here.

