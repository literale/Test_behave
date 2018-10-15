from selenium import webdriver
from behave import *
import time
from datetime import datetime
from selenium.common.exceptions import *


driver = webdriver.Firefox(executable_path=r"geckodriver.exe")

def step_impl(context, site_name):
    """
    :type context: behave.runner.Context
    """
    context.driver.get(site_name)

@step('Кликаем на кнопку Логина')
def step_impl(context):
    log_btn = driver.find_element_by_id('index_login_button')
    log_btn.click()

@step('Прверяем, что не залогинились')
def step_impl(context):
    try:
        log_btn = driver.find_element_by_id('index_login_button')
        with open("log.txt", "a") as log:
            log.write("{0} Мы  не залогинились!\n".format(datetime.now()))
    except NoSuchElementException:
        with open("log.txt", "a") as log:
            log.write("{0} Мы залогинились!\n".format(datetime.now()))
