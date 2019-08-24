# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class LoginPageLocator:
    username_input = (By.XPATH, "//input[@name='login']")
    password_input = (By.XPATH, "//input[@name='password']")
    submit_button = (By.XPATH, "//input[@name='commit']")


class TwoWayAuthenticationPageLocator:
    input_box = (By.XPATH, '//*[@id="otp"]')
    verify_button = (By.XPATH, '//*[@id="login"]/div[5]/form/button')


class CreateRepositoryPageLocator:
    repository_name_input = (By.XPATH, "//input[@name='repository[name]']")
    select_private_radio = (
        By.XPATH,
        '//*[@id="repository_visibility_private"]'
    )
    verify_error_message = '//div[contains(text(), "Two-factor authentication\
         failed.")]'
    submit_button = (By.CSS_SELECTOR, "button.first-in-line")
