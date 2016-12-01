from unittest import TestCase
from selenium import webdriver


class HomepageTestCase(TestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        self.selenium.maximize_window()
        super(HomepageTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(HomepageTestCase, self).tearDown()

    def test_can_visit_homepage(self):
        self.selenium.get('http://10.211.55.26/')
        self.assertIn("Growth Studio - Enjoy Create & Share", self.selenium.title)