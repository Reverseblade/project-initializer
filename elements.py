# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.element = self.find()

    def find(self):
        return WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located(self.locator))

    def click(self):
        self.element = WebDriverWait(
            self.driver, 10).until(
            EC.element_to_be_clickable(self.locator))
        self.element.click()


class InputElement(BaseElement):

    def type(self, keyword):
        self.element.send_keys(keyword)
