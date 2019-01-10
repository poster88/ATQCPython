# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class Test(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox(executable_path="C:\\webdrivers\\geckodriver.exe")
        self.wd.implicitly_wait(60)

    def test_test(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_groups_page(wd)
        self.create_group(wd)
        self.return_to_group_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Вийти").click()

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd):
        wd.find_element_by_link_text("Групи").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("test")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("test header")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("test footer")
        wd.find_element_by_name("submit").click()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("Адреса").click()

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost")

    def tearDown(self):
        self.wd.close()


if __name__ == '__main__':
    unittest.main()
