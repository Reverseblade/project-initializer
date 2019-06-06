# -*- coding: utf-8 -*-

from config import *

from locators import LoginPageLocator
from locators import CreateRepositoryPageLocator

from elements import BaseElement
from elements import InputElement


class BasePage:

    def __init__(self, driver=None, url=None):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.quit()


class LoginPage(BasePage):

    def __init__(self, driver):
        url = GITHUB_LOGIN_PAGE_URL
        super().__init__(driver=driver, url=url)

    @property
    def username_input(self):
        locator = LoginPageLocator.username_input
        return InputElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def password_input(self):
        locator = LoginPageLocator.password_input
        return InputElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def submit_button(self):
        locator = LoginPageLocator.submit_button
        return BaseElement(
            driver=self.driver,
            locator=locator
        )


class CreateRepositoryPage(BasePage):

    def __init__(self, driver):
        url = GITHUB_CREATE_REPOSITORY_PAGE_URL
        super().__init__(driver=driver, url=url)

    @property
    def repository_name_input(self):
        locator = CreateRepositoryPageLocator.repository_name_input
        return InputElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def submit_button(self):
        locator = CreateRepositoryPageLocator.submit_button
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

