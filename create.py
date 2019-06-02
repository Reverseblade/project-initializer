import os
import sys
import time

from selenium import webdriver

from config import *

def create():
    if len(sys.argv) <= 1:
        print('Error: Please enter a project name')
        raise Exception

    browser = webdriver.Chrome('./chromedriver')
    browser.get('http://github.com/login')
    path = "/Users/reverseblade/Code/projects/"
    project_name = str(sys.argv[1])

    try:
        dir_name = path + str(sys.argv[1])
        os.mkdir(path + str(sys.argv[1]))
        print("Directory " , project_name ,  " created ") 
    except FileExistsError:
        print("Directory " , project_name ,  " already exists")

    python_button = browser.find_elements_by_xpath("//input[@name='login']")[0]
    python_button.send_keys(USERNAME)
    python_button = browser.find_elements_by_xpath("//input[@name='password']")[0]
    python_button.send_keys(PASSWORD)
    python_button = browser.find_elements_by_xpath("//input[@name='commit']")[0]
    python_button.click()
    browser.get('https://github.com/new')
    python_button = browser.find_elements_by_xpath("//input[@name='repository[name]']")[0]
    python_button.send_keys(project_name)
    python_button = browser.find_element_by_css_selector('button.first-in-line')
    python_button.submit()
    time.sleep(1)
    browser.quit()
    print('Info: New Github repository "' + project_name + '" reated')

if __name__ == "__main__":
    create()
