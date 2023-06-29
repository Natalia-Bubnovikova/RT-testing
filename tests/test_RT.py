import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from settings import email, password, phone_number, login_name, ls


@pytest.fixture(autouse=True)
def browser_opening():
    # тест-кейс 1
    # проверяем загрузку страницы
    driver = Service("Selenium_edukation/chromedriver/")
    pytest.driver = webdriver.Chrome(service=driver)
    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')
    pytest.driver.implicitly_wait(10)
    yield

    pytest.driver.quit()


def test_presence_of_tabs():
    # тест-кейс 1
    # Проверка наличия таба "Телефон"
    assert pytest.driver.find_element(By.ID, 't-btn-tab-phone').text == "Телефон"
    # Проверка наличия таба "Почта"
    assert pytest.driver.find_element(By.ID, 't-btn-tab-mail').text == "Почта"
    # Проверка наличия таба "Логин"
    assert pytest.driver.find_element(By.ID, 't-btn-tab-login').text == "Логин"
    # Проверка наличия таба "Лицевой счёт"
    assert pytest.driver.find_element(By.ID, 't-btn-tab-ls').text == "Лицевой счёт"


def test_tab_change_phone_mail():
    # тест-кейс 2
    # Тест на проверку автоматической смены таба "Телефон" на таб "Почта"
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-phone')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-phone.rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Мобильный телефон"
    pytest.driver.find_element(By.ID, 'username').send_keys(email)
    pytest.driver.find_element(By.ID, 'password').click()
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Электронная почта"
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-mail.rt-tab.rt-tab--small.rt-tab--active').text == "Почта"


def test_tab_change_phone_login():
    # тест-кейс 3
    # Тест на проверку автоматической смены таба "Телефон" на таб "Логин"
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-phone')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-phone.rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Мобильный телефон"
    pytest.driver.find_element(By.ID, 'username').send_keys(login_name)
    pytest.driver.find_element(By.ID, 'password').click()
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Логин"
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-login.rt-tab.rt-tab--small.rt-tab--active').text == "Логин"


def test_tab_change_phone_ls():
    # тест-кейс 4
    # Тест на проверку автоматической смены таба "Телефон" на таб "Лицевой счёт"
    # Тест провален, так как смены таба не происходит.
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-phone')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-phone.rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Мобильный телефон"
    pytest.driver.find_element(By.ID, 'username').send_keys(ls)
    pytest.driver.find_element(By.ID, 'password').click()
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Лицевой счёт"
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-ls.rt-tab.rt-tab--small.rt-tab--active').text == "Лицевой счёт"


def test_tab_change_mail_phone():
    # тест-кейс 5
    # Тест на проверку автоматической смены таба "Почта" на таб "Мобильный телефон"
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-mail')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-mail.rt-tab.rt-tab--small.rt-tab--active').text == "Почта"
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Электронная почта"
    pytest.driver.find_element(By.ID, 'username').send_keys(phone_number)
    pytest.driver.find_element(By.ID, 'password').click()
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Мобильный телефон"
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-phone.rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"


def test_tab_change_mail_login():
    # тест-кейс 6
    # Тест на проверку автоматической смены таба "Почта" на таб "Логин"
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-mail')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-mail.rt-tab.rt-tab--small.rt-tab--active').text == "Почта"
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Электронная почта"
    pytest.driver.find_element(By.ID, 'username').send_keys(login_name)
    pytest.driver.find_element(By.ID, 'password').click()
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Логин"
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-login.rt-tab.rt-tab--small.rt-tab--active').text == "Логин"


def test_tab_change_mail_ls():
    # тест-кейс 7
    # Тест на проверку автоматической смены таба "Почта" на таб "Лицевой счёт"
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-mail')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-mail.rt-tab.rt-tab--small.rt-tab--active').text == "Почта"
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Электронная почта"
    pytest.driver.find_element(By.ID, 'username').send_keys(ls)
    pytest.driver.find_element(By.ID, 'password').click()
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Лицевой счёт"
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-ls.rt-tab.rt-tab--small.rt-tab--active').text == "Лицевой счёт"


def test_tab_change_login_mail():
    # тест-кейс 8
    # Тест на проверку автоматической смены таба "Логин" на таб "Почта"
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-login')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-login.rt-tab.rt-tab--small.rt-tab--active').text == "Логин"
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Логин"
    pytest.driver.find_element(By.ID, 'username').send_keys(email)
    pytest.driver.find_element(By.ID, 'password').click()
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Электронная почта"
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-mail.rt-tab.rt-tab--small.rt-tab--active').text == "Почта"


def test_tab_change_login_phone():
    # тест-кейс 9
    # Тест на проверку автоматической смены таба "Логин" на таб "Телефон"
    # Тест провален, так как смены таба не происходит.
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-login')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-login.rt-tab.rt-tab--small.rt-tab--active').text == "Логин"
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Логин"
    pytest.driver.find_element(By.ID, 'username').send_keys(phone_number)
    pytest.driver.find_element(By.ID, 'password').click()
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Мобильный телефон"
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-phone.rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"


def test_tab_change_login_ls():
    # тест-кейс 10
    # Тест на проверку автоматической смены таба "Логин" на таб "Лицевой счёт"
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-login')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-login.rt-tab.rt-tab--small.rt-tab--active').text == "Логин"
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Логин"
    pytest.driver.find_element(By.ID, 'username').send_keys(ls)
    pytest.driver.find_element(By.ID, 'password').click()
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Лицевой счёт"
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-ls.rt-tab.rt-tab--small.rt-tab--active').text == "Лицевой счёт"


def test_tab_change_ls_phone():
    # тест-кейс 11
    # Тест на проверку автоматической смены таба "Лицевой счёт" на таб "Телефон"
    # Тест провален, так как смены таба не происходит.
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-ls')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-ls.rt-tab.rt-tab--small.rt-tab--active').text == "Лицевой счёт"
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Лицевой счёт"
    pytest.driver.find_element(By.ID, 'username').send_keys(phone_number)
    pytest.driver.find_element(By.ID, 'password').click()
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Мобильный телефон"
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-phone.rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"


def test_tab_change_ls_mail():
    # тест-кейс 12
    # Тест на проверку автоматической смены таба "Лицевой счёт" на таб "Почта"
    # Тест провален, так как смены таба не происходит.
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-ls')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-ls.rt-tab.rt-tab--small.rt-tab--active').text == "Лицевой счёт"
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Лицевой счёт"
    pytest.driver.find_element(By.ID, 'username').send_keys(email)
    pytest.driver.find_element(By.ID, 'password').click()
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Электронная почта"
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-mail.rt-tab.rt-tab--small.rt-tab--active').text == "Почта"


def test_tab_change_ls_login():
    # тест-кейс 13
    # Тест на проверку автоматической смены таба "Лицевой счёт" на таб "Логин"
    # Тест провален, так как смены таба не происходит.
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-ls')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-ls.rt-tab.rt-tab--small.rt-tab--active').text == "Лицевой счёт"
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Лицевой счёт"
    pytest.driver.find_element(By.ID, 'username').send_keys(login_name)
    pytest.driver.find_element(By.ID, 'password').click()
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder').text == "Логин"
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-login.rt-tab.rt-tab--small.rt-tab--active').text == "Логин"


def test_authorization_phone_correct_data():
    # тест-кейс 14
    # Тест на авторизацию с использованием корректной связки номер телефона+пароль
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-phone')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-phone.rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))).send_keys(phone_number)

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))).send_keys(password)

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button#kc-login'))).click()

    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#app > main > div > div:nth-of-type(2) > div:nth-of-type(3) > h3').text == 'Личные кабинеты'

def test_authorization_phone_incorrect_phone_number():
    # тест-кейс 15
    # Тест на авторизацию с использованием некорректного номера телефона, корректного пароля
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-phone')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-phone.rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))).send_keys('56254985')

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))).send_keys(password)

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button#kc-login'))).click()

    assert pytest.driver.find_element(By.CSS_SELECTOR, 'span#form-error-message').text == 'Неверный логин или пароль'
    assert pytest.driver.find_element(By.ID, 'forgot_password').text == 'Забыл пароль'
    assert pytest.driver.find_element(By.ID, 'forgot_password').value_of_css_property("color") == 'rgba(255, 79, 18, 1)'


def test_authorization_phone_incorrect_pass():
    # тест-кейс 16
    # Тест на авторизацию с использованием корректного номера телефона, некорректного пароля
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-phone')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-phone.rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))).send_keys(phone_number)

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))).send_keys('qwerty13243')

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button#kc-login'))).click()

    assert pytest.driver.find_element(By.CSS_SELECTOR, 'span#form-error-message').text == 'Неверный логин или пароль'
    assert pytest.driver.find_element(By.ID, 'forgot_password').text == 'Забыл пароль'
    assert pytest.driver.find_element(By.ID, 'forgot_password').value_of_css_property("color") == 'rgba(255, 79, 18, 1)'

def test_authorization_phone_incorrect_data():
    # тест-кейс 17
    # Тест на авторизацию с использованием некорректного номера телефона, некорректного пароля
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-phone')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-phone.rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))).send_keys('686846846854')

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))).send_keys('qwerty13243')

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button#kc-login'))).click()

    assert pytest.driver.find_element(By.CSS_SELECTOR, 'span#form-error-message').text == 'Неверный логин или пароль'
    assert pytest.driver.find_element(By.ID, 'forgot_password').text == 'Забыл пароль'
    assert pytest.driver.find_element(By.ID, 'forgot_password').value_of_css_property("color") == 'rgba(255, 79, 18, 1)'


def test_authorization_mail_correct_data():
    # тест-кейс 18
    # Тест на авторизацию с использованием корректной связки номер почта+пароль
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-mail')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-mail.rt-tab.rt-tab--small.rt-tab--active').text == "Почта"
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))).send_keys(email)

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))).send_keys(password)

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button#kc-login'))).click()

    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#app > main > div > div:nth-of-type(2) > div:nth-of-type(3) > h3').text == 'Личные кабинеты'

def test_authorization_mail_incorrect_email():
    # тест-кейс 19
    # Тест на авторизацию с использованием некорректной почты, корректного пароля
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-mail')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-mail.rt-tab.rt-tab--small.rt-tab--active').text == "Почта"

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))).send_keys('test@test.ru')

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))).send_keys(password)

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button#kc-login'))).click()

    assert pytest.driver.find_element(By.CSS_SELECTOR, 'span#form-error-message').text == 'Неверный логин или пароль'
    assert pytest.driver.find_element(By.ID, 'forgot_password').text == 'Забыл пароль'
    assert pytest.driver.find_element(By.ID, 'forgot_password').value_of_css_property("color") == 'rgba(255, 79, 18, 1)'


def test_authorization_mail_incorrect_pass():
    # тест-кейс 20
    # Тест на авторизацию с использованием корректной почты, некорректного пароля
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-mail')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-mail.rt-tab.rt-tab--small.rt-tab--active').text == "Почта"
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))).send_keys(email)

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))).send_keys('qwerty13243')

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button#kc-login'))).click()

    assert pytest.driver.find_element(By.CSS_SELECTOR, 'span#form-error-message').text == 'Неверный логин или пароль'
    assert pytest.driver.find_element(By.ID, 'forgot_password').text == 'Забыл пароль'
    assert pytest.driver.find_element(By.ID, 'forgot_password').value_of_css_property("color") == 'rgba(255, 79, 18, 1)'

def test_authorization_mail_incorrect_data():
    # тест-кейс 21
    # Тест на авторизацию с использованием некорректной почты, некорректного пароля
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-mail')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-mail.rt-tab.rt-tab--small.rt-tab--active').text == "Почта"
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))).send_keys('test@test.ru')

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))).send_keys('qwerty13243')

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button#kc-login'))).click()

    assert pytest.driver.find_element(By.CSS_SELECTOR, 'span#form-error-message').text == 'Неверный логин или пароль'
    assert pytest.driver.find_element(By.ID, 'forgot_password').text == 'Забыл пароль'
    assert pytest.driver.find_element(By.ID, 'forgot_password').value_of_css_property("color") == 'rgba(255, 79, 18, 1)'



def test_authorization_login_correct_data():
    # тест-кейс 22
    # Тест на авторизацию с использованием корректной связки номер логин+пароль
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-login')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-login.rt-tab.rt-tab--small.rt-tab--active').text == "Логин"
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))).send_keys(login_name)

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))).send_keys(password)

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button#kc-login'))).click()

    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#app > main > div > div:nth-of-type(2) > div:nth-of-type(3) > h3').text == 'Личные кабинеты'

def test_authorization_login_incorrect_login():
    # тест-кейс 23
    # Тест на авторизацию с использованием некорректного логина, корректного пароля
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-login')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-login.rt-tab.rt-tab--small.rt-tab--active').text == "Логин"

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))).send_keys('qwerty123456')

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))).send_keys(password)

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button#kc-login'))).click()

    assert pytest.driver.find_element(By.CSS_SELECTOR, 'span#form-error-message').text == 'Неверный логин или пароль'
    assert pytest.driver.find_element(By.ID, 'forgot_password').text == 'Забыл пароль'
    assert pytest.driver.find_element(By.ID, 'forgot_password').value_of_css_property("color") == 'rgba(255, 79, 18, 1)'


def test_authorization_login_incorrect_pass():
    # тест-кейс 24
    # Тест на авторизацию с использованием корректного логина, некорректного пароля
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-login')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-login.rt-tab.rt-tab--small.rt-tab--active').text == "Логин"
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))).send_keys(login_name)

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))).send_keys('qwerty13243')

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button#kc-login'))).click()

    assert pytest.driver.find_element(By.CSS_SELECTOR, 'span#form-error-message').text == 'Неверный логин или пароль'
    assert pytest.driver.find_element(By.ID, 'forgot_password').text == 'Забыл пароль'
    assert pytest.driver.find_element(By.ID, 'forgot_password').value_of_css_property("color") == 'rgba(255, 79, 18, 1)'

def test_authorization_login_incorrect_data():
    # тест-кейс 25
    # Тест на авторизацию с использованием некорректного логина, некорректного пароля
    tab = pytest.driver.find_element(By.ID, 't-btn-tab-login')
    tab.click()
    assert pytest.driver.find_element(By.CSS_SELECTOR,
                                      'div#t-btn-tab-login.rt-tab.rt-tab--small.rt-tab--active').text == "Логин"
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))).send_keys('qwerty123456')

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))).send_keys('qwerty13243')

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button#kc-login'))).click()

    assert pytest.driver.find_element(By.CSS_SELECTOR, 'span#form-error-message').text == 'Неверный логин или пароль'
    assert pytest.driver.find_element(By.ID, 'forgot_password').text == 'Забыл пароль'
    assert pytest.driver.find_element(By.ID, 'forgot_password').value_of_css_property("color") == 'rgba(255, 79, 18, 1)'


def test_forgot_pass_page_presence_elements():
    # тест-кейс 26
    # Тест на проверку наличия табов, кнопок и поля ввода
    pytest.driver.find_element(By.ID, 'forgot_password').click()
    # Проверка наличия таба "Телефон"
    assert pytest.driver.find_element(By.ID, 't-btn-tab-phone').text == "Телефон"
    # Проверка наличия таба "Почта"
    assert pytest.driver.find_element(By.ID, 't-btn-tab-mail').text == "Почта"
    # Проверка наличия таба "Логин"
    assert pytest.driver.find_element(By.ID, 't-btn-tab-login').text == "Логин"
    # Проверка наличия таба "Лицевой счёт"
    assert pytest.driver.find_element(By.ID, 't-btn-tab-ls').text == "Лицевой счёт"
    # Проверка наличия поля ввода капчи
    assert pytest.driver.find_element(By.ID, 'captcha')
    # Проверка наличия кнопки "Продолжить"
    assert pytest.driver.find_element(By.ID, 'reset').text == "Продолжить"
    # Проверка наличия кнопки "Вернуться назад"
    assert pytest.driver.find_element(By.ID, 'reset-back').text == "Вернуться назад"



