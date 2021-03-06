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
        ToDo.objects.create(title = "test1")
        ToDo.objects.create(title = "test2", completed = True)

        response = self.client.get('')  

        self.assertTemplateUsed(response, 'root.html')

        self.assertIn('test1', response.content.decode())
        self.assertIn('test2', response.content.decode())
    
    def test_complete_todo_POST_request_works_well(self):
        ToDo.objects.create(title = "test1")
        
        self.assertFalse(ToDo.objects.first().completed)

        response = self.client.post(
            '/complete_todo/',
            data = {'id' : 1 })

        self.assertTrue(ToDo.objects.first().completed)

    def test_delete_todo_POST_request_works_well(self):
        ToDo.objects.create(title = "test1")

        response = self.client.post(
            '/delete_todo/',
            data = {'id' : 1 })

        self.assertTrue(ToDo.objects.first() == None)


class ToDoModelTest(TestCase):
       
    def test_can_insert_ToDo_well(self):
        
        name= "test"
        completed = False
        contents = "for test!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        ToDo.objects.create(title = name, completed = completed, priority = 2, due = date.today(),
            contents = contents)

        td = ToDo.objects.first()

        self.assertEqual(td.title ,name)
        self.assertFalse(td.completed)
        self.assertEqual(td.priority, 2)
        self.assertEqual(td.due , date.today())
        self.assertEqual(td.contents , contents)

class AddAndEditToDoTest(TestCase):

    def test_can_save_and_process_add_todo_POST_request(self):
        
        response = self.client.post(
            '/add_todo/',
            data = {'todo_title' : 'test',
                    'todo_priority': 3,
                    'todo_due' : date.today(),
                    'todo_contents': "it's contents!!"
        })

        saved_td = ToDo.objects.first()

        self.assertEqual(saved_td.title, 'test')
        self.assertEqual(saved_td.priority, 3)
        self.assertEqual(saved_td.due , date.today())
        self.assertEqual(saved_td.contents, "it's contents!!")
        
    def test_can_process_edit_POST_request(self):
        ToDo.objects.create(title = 'test1', priority = 2)

        response = self.client.post(
            '/edit_todo/',
            data = {'id' : 1,
                    'todo_title' : 'test1',
                    'todo_priority': 3,
                    'todo_due' : date.today(),
                    'todo_contents' : "it's contents!!"
        })

        saved_td = ToDo.objects.first()

        self.assertEqual(saved_td.title, 'test1')
        self.assertEqual(saved_td.priority, 3)
        self.assertEqual(saved_td.due , date.today())
        self.assertEqual(saved_td.contents, "it's contents!!")
        

    def test_can_process_uncomplete_POST_requset(self):
        ToDo.objects.create(title = "test2",  completed = True)

        response = self.client.post(
            '/uncomplete_todo/',
            data = {'id' : 1}
        )

        saved_td = ToDo.objects.first()

        self.assertEqual(saved_td.title, 'test2')
        self.assertFalse(saved_td.completed)
        