from .base_page import BasePage
from .locators import BasketPageLocators


class ProductPage(BasePage):
    def go_to_click_in_basket(self):
        click_basket = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        click_basket.click()

        assert self.browser.find_element()

