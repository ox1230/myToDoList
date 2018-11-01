from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import root
from lists.models import ToDo
from datetime import date, timedelta

from unittest import skip
import re

# Create your tests here.
def remove_csrf_tag(text):
    """Remove csrf tag from TEXT"""
    return re.sub(r'<[^>]*csrfmiddlewaretoken[^>]*>', '', text)
    
class ListsViewTest(TestCase):

    def test_root_url_resolves_root_page_correctly(self):
        
        response = self.client.get('')  

        self.assertTemplateUsed(response, 'root.html')

class ToDoModelTest(TestCase):
       
    def test_can_insert_ToDo_well(self):
        
        name= "test"

        ToDo.objects.create(text = name)

        td = ToDo.objects.first()

        self.assertEqual(td.text ,name)

class AddToDoTest(TestCase):
    """ """

    def test_can_save_and_process_add_todo_POST_request(self):
        
        response = self.client.post(
            '/add_todo/',
            data = {'name' : 'test'
        })

        saved_history = ToDo.objects.first()

        self.assertEqual(saved_history.text, 'test')

