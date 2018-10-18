from selenium.webdriver.common.by import By

buttons_log = {
    "Логин" : (By.ID, 'index_login_button'),
    "Продолжить регистрацию" : (By.ID, 'ij_submit'),
    "Забыли пароль?" : (By.ID, 'index_forgot')
}
buttons_error = {
    "Логин": (By.ID, 'login_button'),
    "Регистрация": (By.ID, 'login_reg_button')
}