from Tools.scripts.win_add2path import PATH
from selenium import webdriver
from behave import *
import time
from datetime import datetime
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                    filename="log.log", level=logging.INFO)

@when('Зашли на сайт "{site_name}"')
def step_impl(context, site_name):
    """
    :type context: behave.runner.Context
    """
    #context.driver = webdriver.Firefox(executable_path=r"D:\\gecodrive\\geckodriver.exe")
    context.driver = webdriver.Firefox(executable_path=r"geckodriver.exe")
    context.driver.get(site_name)
    context.driver.delete_all_cookies()

@step('Кликаем на кнопку Логина')
def step_impl(context):
    log_btn = context.driver.find_element_by_id('index_login_button')
    log_btn.click()

@step('Прверяем, что не залогинились')
def step_impl(context):
    try:
        log_btn = context.driver.find_element_by_id('index_login_button')
        logging.info('Мы  не залогинились!')
        #print("Мы  не залогинились!")
    except NoSuchElementException:
        logging.info('Мы залогинились!')
        #print("Мы залогинились!")

@then('Вводим логин "{login}"')
def step_impl(context, login):
    input_em = context.driver.find_element_by_id('index_email')
    input_em.send_keys(login)


@then('Вводим пароль "{password}"')
def step_impl(context, password):
    input_pass = context.driver.find_element_by_id('index_pass')
    input_pass.send_keys('password')

@then('Приверяем страницу')
def step_impl(context):
    wait_for_element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login_reg_button"))
    )
    if context.driver.current_url == "https://vk.com/":
        logging.info('Мы Не сменили страницу!')
        #print("Мы Не сменили страницу!")
    else:
        logging.info('Мы сменили страницу!')
        #print("Мы сменили страницу!")

    try:
        log_mes_btn = context.driver.find_element_by_id('login_message')
        logging.info('Мы на странице ошибки!')
        #print("Мы на странице ошибки!")
    except NoSuchElementException:
        logging.info('Мы залогинились?')
       # print("Мы залогинились?")


@step('Нажимаем кнопку регистрации')
def step_impl(context):
    log_btn = context.driver.find_element_by_id('login_reg_button')
    log_btn.click()


@step('Опять проверяем страницу')
def step_impl(context):
    wait_for_element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "ij_submit"))
    )
    if context.driver.current_url == "https://vk.com/":
        logging.info('Мы на первой странице!')
       # print("Мы на первой странице!")
    elif context.driver.current_url == "https://vk.com/join":
        logging.info('Мы не на первой странице, но на ее аналоге.')
       # print("Мы не на первой странице, но на ее аналоге.")
    else:
        logging.info('Мы не на первой странице! :с')
       # print("Мы не на первой странице! :с")


def skip_scenario(context, result):
    logging.info('Сценарий не выполнен')