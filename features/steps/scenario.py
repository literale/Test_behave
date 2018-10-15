from selenium import webdriver
from behave import *
import time
from datetime import datetime
from selenium.common.exceptions import *


@when('Зашли на сайт "{site_name}"')
def step_impl(context, site_name):
    """
    :type context: behave.runner.Context
    """
    context.driver = webdriver.Firefox(executable_path=r"D:\\gecodrive\\geckodriver.exe")
    context.driver.get(site_name)

@step('Кликаем на кнопку Логина')
def step_impl(context):
    log_btn = context.driver.find_element_by_id('index_login_button')
    log_btn.click()

@step('Прверяем, что не залогинились')
def step_impl(context):
    try:
        log_btn = context.driver.find_element_by_id('index_login_button')
        print("Мы  не залогинились!")
    except NoSuchElementException:
        print("Мы залогинились!")

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
    wait_for_element = context.WebDriverWait(context.driver, 10).until(
        context.EC.visibility_of_element_located((context.By.ID, "login_reg_button")))
    if context.driver.current_url == "https://vk.com/":
        print("Мы Не сменили страницу!")
    else:
        print("Мы сменили страницу!")
    try:
        log_mes_btn = context.driver.find_element_by_id('login_message')
        print("Мы на странице ошибки!")
    except NoSuchElementException:
        print("Мы залогинились?")


@step('Нажимаем кнопку регистрации')
def step_impl(context):
    log_btn = context.driver.find_element_by_id('login_reg_button')
    log_btn.click()


@step('Опять проверяем страницу')
def step_impl(context):
    wait_for_element = context.WebDriverWait(context.driver, 10).until(
        context.EC.visibility_of_element_located((context.By.ID, "ij_submit"))
    )
    if context.driver.current_url == "https://vk.com/":
        print("Мы на первой странице!")
    elif context.driver.current_url == "https://vk.com/join":
        print("Мы не на первой странице, но на ее аналоге.")
    else:
        print("Мы не на первой странице! :с")


def skip_scenario(context, result):
    if result == "Неудачно":
        with open("log.txt", "a") as log:
            log.write("{0} Сценарий не выполнен.\n".format(datetime.now()))
            context.scenario.skip(require_not_executed=True)