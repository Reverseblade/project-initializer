import os
import sys
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from config import *

from pages import LoginPage
from pages import CreateRepositoryPage

import logging
logging.basicConfig(level=logging.INFO)

if len(sys.argv) <= 1:
    raise Exception('Please enter a project name')

project_name = str(sys.argv[1])

try:
    os.mkdir(PROJECT_PATH + project_name)
    logging.info("Directory {} created".format(project_name))
    print()
except FileExistsError:
    raise FileExistsError("Directory " + project_name + " already exists")

# Log in to Github
driver = webdriver.Chrome('./chromedriver')
login_page = LoginPage(driver)
login_page.open()
login_page.username_input.type(GITHUB_USERNAME)
login_page.password_input.type(GITHUB_PASSWORD)
login_page.submit_button.click()

# Create a new repository
create_repository_page = CreateRepositoryPage(driver)
create_repository_page.open()
create_repository_page.repository_name_input.type(project_name)

try:
    create_repository_page.submit_button.click()
except TimeoutException:
    raise TimeoutException('The repository {} already exists on this account'.format(project_name))

# Check if a new repository was created
current_url = create_repository_page.driver.current_url
new_repository_url = 'https://github.com/{0}/{1}'.format(GITHUB_USERNAME, project_name)
create_repository_page.close()

if current_url != new_repository_url:
    raise Exception('Failed to create a new Github repository')
else:
    logging.info('New Github repository {} created'.format(project_name))
