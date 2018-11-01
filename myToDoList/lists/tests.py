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
        ToDo.objects.create(text = "test1")

        response = self.client.get('')  

        self.assertTemplateUsed(response, 'root.html')

        self.assertIn('test1', response.content.decode())

    def test_complete_todo_POST_request_works_well(self):
        ToDo.objects.create(text = "test1")
        
        self.assertFalse(ToDo.objects.first().completed)

        response = self.client.post(
            '/complete_todo/',
            data = {'id' : 1
        })

        self.assertTrue(ToDo.objects.first().completed)


class ToDoModelTest(TestCase):
       
    def test_can_insert_ToDo_well(self):
        
        name= "test"
        completed = False

        ToDo.objects.create(text = name, completed = completed)

        td = ToDo.objects.first()

        self.assertEqual(td.text ,name)
        self.assertFalse(td.completed)

class AddToDoTest(TestCase):
    """ """

    def test_can_save_and_process_add_todo_POST_request(self):
        
        response = self.client.post(
            '/add_todo/',
            data = {'todo_text' : 'test'
        })

        saved_history = ToDo.objects.first()

        self.assertEqual(saved_history.text, 'test')
