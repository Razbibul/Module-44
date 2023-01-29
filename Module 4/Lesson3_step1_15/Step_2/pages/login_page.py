from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        #assert self.browser.current_url(*LoginPageLocators.LOGIN_AUTORIZED)
        login_authoriz = self.browser.find_element(*LoginPageLocators.LOGIN_AUTHORIZED)  # обращаемся к браузеру с помощью self т.к. он хранится в BasePage из base_page.py
        #assert self.browser.current_url(*LoginPageLocators.LOGIN_AUTHORIZED) "Нет такой ссылки"
        login_authoriz.click()
        time.sleep(3)
        #self.browser.current_url.click()

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORMA), "НЕТ ФОРМЫ АВТОРИЗАЦИИ ДАУН"
        #assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.ATHORIZED_FORMA), "НЕТ ФОРМЫ РЕГИСТРАЦИИ ДАУН"
        #assert True