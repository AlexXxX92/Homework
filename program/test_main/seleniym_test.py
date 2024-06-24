from selenium import webdriver
from selenium.common import  NoSuchElementException
from selenium.webdriver.common.by import By
import pytest



driver = webdriver.Chrome()
driver.implicitly_wait(5)

@pytest.mark.parametrize(
    'login, pass_, result',
    (['czfvsd', ' ', 'Нет такого аккаунта. Проверьте логин или войдите по телефону'],
     ['', ' ', 'Логин не указан'],
     ['   324', ' ', 'Такой логин не подойдет'],
     ['xxx', '000', 'Неверный пароль'],
     ['xxx', ' ', 'Пароль не указан'],
     ['', '', "Подтвердите кодом из пуш-уведомления"] #Нужны валидные логин и пароль
    ))
def test_ya_login(login, pass_, result):
    driver.get('https://passport.yandex.ru/auth/')
    driver.find_element(By.NAME, value='login').send_keys(login)
    driver.find_element(By.XPATH, value="//button[@id='passp:sign-in']").click()

    try:
        driver.find_element(By.NAME, value='passwd').send_keys(pass_)
        driver.find_element(By.XPATH, value="//button[@id='passp:sign-in']").click()

        try:
            correct = driver.find_element(By.CLASS_NAME, value='TitleWithDescription '
                                                               'TitleWithDescription_marginBottom_24')

        except NoSuchElementException:
            error_pass = driver.find_element(By.XPATH, value="//div[@id='field:input-passwd:hint']")
            assert error_pass.text == result
        else:
            assert result in correct.text
    except NoSuchElementException:
        error_login = driver.find_element(By.XPATH, value="//div[@id='field:input-login:hint']")
        assert error_login.text == result
