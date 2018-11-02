from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from lists.models import ToDo
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions

import unittest
import time
from datetime import date, timedelta

class BaseTest(LiveServerTestCase):
    def setUp(self):
        """테스트 시작 전에 수행"""
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)   # 암묵적 대기 -- 1초
        
        ToDo.objects.create(text = "어제 등록한 할 일")
    def tearDown(self):
        """테스트 후에 시행-- 테스트에 에러가 발생해도 실행된다"""
        self.browser.quit()
    
  
    def go_to_page(self,page:str):
        """ 원하는 페이지로 이동한다"""
        menu = self.browser.find_element_by_id("{}_menu".format(page))
        menu.click()

        # WebDriverWait(self.browser, 3).until(
        #     expected_conditions.text_to_be_present_in_element(
        #     (By.ID, 'thing-on-new-page'),
        #     'expected new text'
        #     )
        # )
        time.sleep(1)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/{}/'.format(page))

    def find_rows_from_table_id(self, id):
        """id에서 tr을 뽑아낸 후 각 row에서 text를 뽑아내 row별 리스트로 만들어 리턴한다."""
        table = self.browser.find_element_by_id(id)
        rows = table.find_elements_by_tag_name('tr')
        return [row.text for row in rows]

class VisitorTest(BaseTest):
        
    def test_todo_and_can_see_it(self):
        """기본기능이 제대로 되는지 테스트한다. ( todo 입력+ 우선순위 설정 + 날짜 설정, 보기)"""

        #edith가 해당 웹사이트 방문
        self.browser.get(self.live_server_url)

        # 이름은 myToDoList이다.
        assert 'myToDoList' in self.browser.title

        # "ToDoList 만들기- 매우 중요"를 입력, dueDate는 2018-11-4일까지
        self.browser.find_element_by_id("todo_inputBox").send_keys("ToDoList 만들기")
        el = self.browser.find_element_by_id('priority_selectBox')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == '매우 중요':
                option.click() 
                break
        self.browser.find_element_by_id("todo_due_inputBox").send_keys("2018-11-04")
        self.browser.find_element_by_id("add_todo_button").click()
        

        # 페이지가 갱신되면서 "ToDoList 만들기"가 텍스트 상자에 입력됨
        rows_text = self.find_rows_from_table_id("todo_textBox")
        self.assertIn('~Nov. 4, 2018 ToDoList 만들기 매우 중요', rows_text)
        


    def test_completed_button_work_well(self):
        """ 완료 처리가 제대로 되는지 체크한다. """

        #edith가 해당 웹사이트 방문
        self.browser.get(self.live_server_url)

        # "어제 등록한 할 일"를 완료함
        self.browser.find_element_by_id("어제 등록한 할 일_complete_button").click()

        # # 페이지가 갱신되면서 "ToDoList 만들기"가 완료된 todo로 이동함
        rows_text = self.find_rows_from_table_id("todo_textBox")
        self.assertNotIn('어제 등록한 할 일 보통', rows_text)
        
        rows_text2 = self.find_rows_from_table_id("todo_complete_textBox")
        self.assertIn('어제 등록한 할 일', rows_text2)

    def test_delete_button_work_well(self):
        """ 삭제 처리가 제대로 되는지 체크한다"""
        #edith가 해당 웹사이트 방문
        self.browser.get(self.live_server_url)

        #"어제 등록한 할일"이 보인다.
        rows_text = self.find_rows_from_table_id("todo_textBox")
        self.assertIn('어제 등록한 할 일 보통', rows_text)
        
        # "어제 등록한 할 일"를 삭제함
        self.browser.find_element_by_id("어제 등록한 할 일_delete_button").click()

        # "어제 등록한 할 일"이 어디에도 보이지 않는다.
        rows_text = self.find_rows_from_table_id("todo_textBox")
        self.assertNotIn('어제 등록한 할 일 보통', rows_text)
        
        rows_text = self.find_rows_from_table_id("todo_complete_textBox")
        self.assertNotIn('어제 등록한 할 일', rows_text)
        
