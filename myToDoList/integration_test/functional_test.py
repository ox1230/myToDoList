from selenium import webdriver
from integration_test.base import FunctionalTest

class VisitorTest(FunctionalTest):
        
    def test_todo_and_can_see_it(self):
        """기본기능이 제대로 되는지 테스트한다. ( todo 입력, 보기)"""

        #edith가 해당 웹사이트 방문
        self.browser.get(self.live_server_url)

        # 이름은 myToDoList이다.
        assert 'myToDoList' in self.browser.title

        # "ToDoList 만들기"를 텍스트 상자에 입력
        self.browser.find_element_by_id("todo_inputBox").send_keys("ToDoList 만들기")

        # 페이지가 갱신되면서 "ToDoList 만들기"가 텍스트 상자에 입력됨
        rows_text = self.find_rows_from_table_id("todo_textBox")
        self.assertIn('ToDoList 만들기', rows_text)