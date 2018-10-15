from behave import *
from selenium import webdriver
import time
from datetime import datetime
from selenium.common.exceptions import *

with open("log.txt", "a") as log:
    log.write("{0} Сценарий выполнен.\n".format(datetime.now()))


@when('Зашли на сайт "{site_name}"')
def step_impl(context, site_name):
    """
    :type context: behave.runner.Context
    """
    # context.driver.get("http://google.ru")
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.driver.get(site_name)

@step('Кликаем на кнопку Логина')
def step_impl(context):
    log_btn = driver.find_element_by_id('index_login_button')
    log_btn.click()

@step('Прверяем, что не залогинились')
def step_impl(context):
    try:
        log_btn = driver.find_element_by_id('index_login_button')
        log.write("{0} Мы  не залогинились!\n".format(datetime.now()))
    except NoSuchElementException:
        log.write("{0} Мы залогинились!\n".format(datetime.now()))
