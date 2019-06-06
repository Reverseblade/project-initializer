# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class LoginPageLocator:
    username_input = (By.XPATH, "//input[@name='login']")
    password_input = (By.XPATH, "//input[@name='password']")
    submit_button = (By.XPATH, "//input[@name='commit']")


class CreateRepositoryPageLocator:
    repository_name_input = (By.XPATH, "//input[@name='repository[name]']")
    submit_button = (By.CSS_SELECTOR, "button.first-in-line")

