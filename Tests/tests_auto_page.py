from locators import *
from settings import *

def test_autorisation_with_phone(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_PHONE_FIELD_ACTIV).send_keys(valid_phone)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_LK_TAB).text == 'Личный кабинет'
    print("\nАвторизация по номеру телефона прошла успешно ")
    print("\nТест № TC_FAR-008 пройден")

def test_autorisation_with_fake_phone(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_PHONE_FIELD_ACTIV).send_keys(fake_phone)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR).text == 'Неверный логин или пароль'
    print("\n При введении невалидного номера телефона появляется надпись 'Неверный логин или пароль'")

def test_autorisation_with_invalid_password(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_PHONE_FIELD_ACTIV).send_keys(valid_phone)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(fake_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR).text == 'Неверный логин или пароль'
    print("\n При введении невалидного пароля появляется надпись 'Неверный логин или пароль'")

def test_autorisation_with_no_phone(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_PHONE_FIELD_ACTIV).send_keys()
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR_MESS).text == 'Введите номер телефона'
    print("\n При отсутствии номера телефона появится надпись 'Введите номер телефона'")
    print("\nТест № TC_FAR-009 пройден")


def test_autorisation_with_mail(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_FIELD_ACTIV).send_keys(valid_email)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_LK_TAB).text == 'Личный кабинет'
    print("\nАвторизация по адресу электронной почты прошла успешно ")
    print ("\nТест № TC_FAR-010 Пройден")

def test_autorisation_with_fake_mail(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_FIELD_ACTIV).send_keys(fake_email)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR).text == 'Неверный логин или пароль'
    print("\n При введении невалидного адреса электронной почты появляется надпись 'Неверный логин или пароль'")

def test_autorisation_with_invalid_mail_password(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_FIELD_ACTIV).send_keys(valid_email)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(fake_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR).text == 'Неверный логин или пароль'
    print("\n При введении невалидного пароля появляется надпись 'Неверный логин или пароль'")

def test_autorisation_with_no_mail(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_FIELD_ACTIV).send_keys()
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR_MESS).text == 'Введите адрес, указанный при регистрации'
    print("\n При отсутствии адреса электронной почты появляется надпись 'Введите адрес, указанный при регистрации'")
    print("\nТест № TC_FAR-011 с невалидными данными пройден")


def test_autorisation_with_login(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_FIELD_ACTIV).send_keys(valid_login)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_LK_TAB).text == 'Личный кабинет'
    print("\nАвторизация по логину прошла успешно ")
    print ("\nТест № TC_FAR-012 Пройден")


def test_autorisation_with_fake_login(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_FIELD_ACTIV).send_keys(fake_login)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR).text == 'Неверный логин или пароль'
    print("\n При введении невалидного логина появляется надпись 'Неверный логин или пароль'")

def test_autorisation_with_invalid_login_password(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_FIELD_ACTIV).send_keys(valid_login)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(fake_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR).text == 'Неверный логин или пароль'
    print("\n При введении невалидного пароля появляется надпись 'Неверный логин или пароль'")

def test_autorisation_with_no_login(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_FIELD_ACTIV).send_keys()
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR_MESS).text == 'Введите логин, указанный при регистрации'
    print("\n При отсутствии логина появляется надпись 'Введите логин, указанный при регистрации'")
    print("\nТест № TC_FAR-013 с невалидными данными пройден")


def test_autorisation_with_ls(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_LS_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LS_FIELD_ACTIV).send_keys(valid_ls)
    rowser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_LK_TAB).text == 'Личный кабинет'
    print("\nАвторизация по номеру лицевого счета прошла успешно ")
    print ("\nТест № TC_FAR-014 Пройден")


def test_autorisation_with_invalid_ls(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_LS_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LS_FIELD_ACTIV).send_keys(invalid_ls)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR).text == 'Неверный логин или пароль'
    print("\n При введении невалидного номера лицевого счета появляется надпись 'Неверный логин или пароль'")

def test_autorisation_with_invalid_password_ls(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_LS_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LS_FIELD_ACTIV).send_keys(valid_ls)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(fake_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR).text == 'Неверный логин или пароль'
    print("\n При введении невалидного пароля появляется надпись 'Неверный логин или пароль'")

def test_autorisation_with_no_ls(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_LS_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LS_FIELD_ACTIV).send_keys()
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR_MESS).text == 'Введите номер вашего лицевого счета'
    print("\n При отсутствии номера лицевого счета появляется надпись 'Введите номер вашего лицевого счета'")
    print("\nТест № TC_FAR-015 с невалидными данными пройден")

