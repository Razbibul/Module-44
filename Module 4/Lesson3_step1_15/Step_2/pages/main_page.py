from .base_page import BasePage
#from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.BASKET_BUTTON), "АААААААААААА НЕТ КНОПКИ. аааааааааааааа"
