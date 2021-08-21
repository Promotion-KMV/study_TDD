# import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        print('start')
        self.browser = webdriver.Firefox()
        # self.browser = webdriver.Firefox(executable_path="/home/vlad/study_Django/study_TDD/geckodriver")
        self.browser.get('http://localhost:8000')

    def tearDown(self):
        print('finish')
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        # self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Hello', header_text)
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        input_box.send_keys('Купить павлиньи перья')
        input_box.send_keys(Keys.ENTER)
        time.sleep(2)
        # self.check_for_row_in_list_table('1: Купить павлиньи перья')
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Сделать мушку из павлиньих перьев')
        input_box.send_keys(Keys.ENTER)
        time.sleep(2)
        self.check_for_row_in_list_table('1: Купить павлинья перья')
        self.check_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')

        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn('1: Купить павлиньи перья', [row.text for row in rows])
        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn(
        #     '2 : Сделать мушку из павлиних перьев',
        #     [row.text for row in rows]
        # )


if __name__ == '__main__':
    unittest.main(warnings='ignore')