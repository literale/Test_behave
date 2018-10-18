import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from io import BytesIO
from tkinter import Image

import location as location
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

from features.steps import elements

logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                    filename="log.log", level=logging.INFO)
page: str

@when('Зашли на сайт "{site_name}"')
def step_impl(context, site_name):
    """
    :type context: behave.runner.Context
    """
    #context.driver = webdriver.Firefox(executable_path=r"D:\\gecodrive\\geckodriver.exe")
    context.driver = webdriver.Firefox(executable_path=r"geckodriver.exe")
    context.driver.get(site_name)
    context.driver.delete_all_cookies()
    global page
    page= "Логин"

    @step('Кликаем на кнопку "{buttom}"')
    def step_impl(context, buttom):
        global page
        if page == "Логин" :
            xp = elements.buttons_log[buttom]
        elif page == "Ошибка":
            xp = elements.buttons_error[buttom]
        log_btn = context.driver.find_element(xp[0], xp[1])
        log_btn.click()


@step('Кликаем на кнопку Логина')
def step_impl(context):
    log_btn = context.driver.find_element_by_id('index_login_button')
    log_btn.click()

@step('Прверяем, что не залогинились')
def step_impl(context):
    global page
    try:
        log_btn = context.driver.find_element_by_id('index_login_button')
        logging.info('Мы  не залогинились!')
        page = "Логин"
        #print("Мы  не залогинились!")
    except NoSuchElementException:
        logging.info('Мы залогинились!')
        page = "Ват"
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
    global page
    wait_for_element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login_reg_button"))
    )
    if context.driver.current_url == "https://vk.com/":
        logging.info('Мы Не сменили страницу!')
        page = "Логин"
        #print("Мы Не сменили страницу!")
    else:
        logging.info('Мы сменили страницу!')
        page = "ХЗ"
        #print("Мы сменили страницу!")

    try:
        log_mes_btn = context.driver.find_element_by_id('login_message')
        page = "Ошибка"
        logging.info('Мы на странице ошибки!')

        #print("Мы на странице ошибки!")
    except NoSuchElementException:
        logging.info('Мы залогинились?')
        page = "Ват"
       # print("Мы залогинились?")

@step('Сделаем скриншот "{name}" и отправим на почту "{to_user}"')
def step_impl(context, name, to_user):
    screenshot = context.driver.save_screenshot("screеnshots/" + name + ".jpg")   # ругается, но сохраняет
    send_msg_scr(to_user, name)


def send_msg_scr(to_user, scr_name):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login("GlebovaPyton@gmail.com", "TestPyton6!")
    msg = MIMEMultipart()
    part = MIMEApplication(open("screеnshots/" + scr_name + ".jpg", 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="screеnshots/" + scr_name + ".jpg")
    msg.attach(part)
    smtpObj.sendmail("GlebovaPyton@gmail.com", to_user, msg.as_string())
    smtpObj.quit()
    os.remove("screеnshots/" + scr_name + ".jpg")

@step('Нажимаем кнопку регистрации')
def step_impl(context):
    log_btn = context.driver.find_element_by_id('login_reg_button')
    log_btn.click()


@step('Опять проверяем страницу')
def step_impl(context):
    global page
    wait_for_element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "ij_submit"))
    )
    if context.driver.current_url == "https://vk.com/":
        logging.info('Мы на первой странице!')
        page = "Логин"
       # print("Мы на первой странице!")
    elif context.driver.current_url == "https://vk.com/join":
        logging.info('Мы не на первой странице, но на ее аналоге.')
        page = "Логин"
       # print("Мы не на первой странице, но на ее аналоге.")
    else:
        logging.info('Мы не на первой странице! :с')
        page = "Ват"
       # print("Мы не на первой странице! :с")


def skip_scenario(context, result):
    name = "error_screenshot"
    screenshot = context.driver.save_screenshot("screеnshots/" + name + ".jpg")
    send_msg_scr("Literallle@yandex.ru", "error_screenshot")
    logging.info('Сценарий не выполнен')