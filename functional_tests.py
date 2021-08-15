# import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        print('ok')
        self.browser = webdriver.Firefox()

    def tearDown(self):
        print('finish')
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        time.sleep(2)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Hello', header_text)


if __name__ == '__main__':
    unittest.main(warnings='ignore')