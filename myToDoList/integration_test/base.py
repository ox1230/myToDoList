from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
#from main.models import Category,History
#from main.process import db_reset ,WeekAndDay
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions

import unittest
import time
from datetime import date, timedelta

class FunctionalTest(LiveServerTestCase):
    def setUp(self):
        """테스트 시작 전에 수행"""
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)   # 암묵적 대기 -- 1초
        
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