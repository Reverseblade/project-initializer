import os
import sys

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

import config

from pages import LoginPage
from pages import CreateRepositoryPage
from pages import TwoWayAuthenticationPage

import logging
logging.basicConfig(level=logging.INFO)

# handle argument
if len(sys.argv) <= 1:
    raise Exception('Please enter your project name')
project_name = str(sys.argv[1])

# set driver
chrome_options = Options()
if config.IS_HEADLESS:
    chrome_options.add_argument("--headless")

executable_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'chromedriver'
    )

driver = webdriver.Chrome(
        executable_path=executable_path,
        options=chrome_options
    )

# login to Github
login_page = LoginPage(driver)
login_page.open()
login_page.username_input.type(config.GITHUB_USERNAME)
login_page.password_input.type(config.GITHUB_PASSWORD)
login_page.submit_button.click()
logging.info('Logged in to Github OK!')

# two-way authentication
if config.HAS_TWO_WAY_AUTHENTICATION:
    auth_code = input('Enter your verification code: ')
    two_way_auth_page = TwoWayAuthenticationPage(login_page.driver)
    two_way_auth_page.input_box.type(auth_code)
    two_way_auth_page.verify_button.click()
    logging.info('two-way authentication OK!')

# create a new repository
create_repository_page = CreateRepositoryPage(driver)
create_repository_page.open()
create_repository_page.select_private_radio.click()
create_repository_page.repository_name_input.type(project_name)

try:
    create_repository_page.submit_button.click()
except TimeoutException:
    raise TimeoutException('The repository named {} already exists \
                           on this account'.format(project_name))

if create_repository_page.has_veryify_error_text == True:
    auth_code = input('Enter your verification code: ')
    two_way_auth_page = TwoWayAuthenticationPage(login_page.driver)
    two_way_auth_page.input_box.type(auth_code)
    two_way_auth_page.verify_button.click()
    logging.info('two-way authentication OK!')

current_url = create_repository_page.driver.current_url

new_repository_url = 'https://github.com/{0}/{1}'.format(
        config.GITHUB_USERNAME,
        project_name
    )

create_repository_page.close()

if current_url != new_repository_url:
    raise Exception('Failed to create a new Github repository')

logging.info('New github repository named {} created'.format(project_name))
