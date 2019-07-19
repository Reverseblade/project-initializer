import os
import sys
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

from config import *

from pages import LoginPage
from pages import CreateRepositoryPage

import logging
logging.basicConfig(level=logging.INFO)

# handle argument
if len(sys.argv) <= 1:
    raise Exception('Please enter your project name')
project_name = str(sys.argv[1])

# set driver
chrome_options = Options()
if IS_HEADLESS:
    chrome_options.add_argument("--headless")

executable_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'chromedriver'
    )

driver = webdriver.Chrome(
        executable_path=executable_path,
        options=chrome_options
    )

# log in to Github
login_page = LoginPage(driver)
login_page.open()
login_page.username_input.type(GITHUB_USERNAME)
login_page.password_input.type(GITHUB_PASSWORD)
login_page.submit_button.click()
logging.info('Logged in to Github')

# create a new repository
create_repository_page = CreateRepositoryPage(driver)
create_repository_page.open()
create_repository_page.repository_name_input.type(project_name)

try:
    create_repository_page.submit_button.click()
except TimeoutException:
    raise TimeoutException('The repository named {} already exists \
                           on this account'.format(project_name))

# check if new repository created
current_url = create_repository_page.driver.current_url
new_repository_url = 'https://github.com/{0}/{1}'.format(
        GITHUB_USERNAME,
        project_name
    )

create_repository_page.close()

if current_url != new_repository_url:
    raise Exception('Failed to create a new Github repository')

logging.info('New github repository named {} created'.format(project_name))
