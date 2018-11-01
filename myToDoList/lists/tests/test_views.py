from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
#from lists.views import home_page
#from lists.models import Todo
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

     

class AddToDoTest(TestCase):
    """ 일단 capql에서 가져온 재활용"""
    @skip
    def test_add_history_url_resolve_add_history_page_correctly(self):

        Category.objects.create(name = '첫번째')
        Category.objects.create(name = '거래내역분류')  #카테고리 확인용
        
        response = self.client.get('/add_history/')  

        self.assertTemplateUsed(response, 'add_history.html')

        self.assertContains(response,'첫번째')
        self.assertContains(response,'거래내역분류')

    @skip
    def test_can_save_and_process_add_history_POST_request_and_go_main(self):
        
        cate_ = Category.objects.create(name = '거래내역분류')
 
        response = self.client.post(
            '/add_history/',
            data = {'category': cate_.id,
                    'name' : '거래내역내용',
                    'price' : '1000',
                    'written_date': date.today(),
        })

        saved_history = History.objects.first()

        self.assertEqual(saved_history.category ,cate_ )
        self.assertEqual(saved_history.name , '거래내역내용')
        self.assertEqual(saved_history.price , 1000)
        self.assertEqual(saved_history.written_date , date.today())

        self.assertRedirects(response, '/main/')


