# import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from django.test import LiveServerTestCase
import time
import unittest

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        print('start')
        # self.browser = webdriver.Firefox()
        self.browser = webdriver.Firefox(executable_path="/home/vlad/study_Django/study_TDD/geckodriver")
        self.browser.get(self.live_server_url)

    def tearDown(self):
        print('finish')
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                time.sleep(1)
                return
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Купить павлиньи перья')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Купить павлиньи перья')
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Сделать мушку из павлиньих перьев')
        input_box.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')
        self.wait_for_row_in_list_table('1: Купить павлиньи перья')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        self.browser.get(self.live_server_url)
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Купить павлиньи перья')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Купить павлиньи перья')
        edit_list_url = self.browser.current_url
        self.assertRegex(edit_list_url, '/lists/.+')

        self.browser.quit()
        self.browser = webdriver.Firefox(executable_path="/home/vlad/study_Django/study_TDD/geckodriver")
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Купть павлиньи перья', page_text)
        self.assertNotIn('Cдеgit лать мушку', page_text)

        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Купить молоко')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Купить молоко')

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edit_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Купить павлиньи перья', page_text)
        self.assertIn('Купить молоко', page_text)
        time.sleep(2)

#
# if __name__ == '__main__':
#     unittest.main(warnings='ignore')