from selenium.webdriver.common.by import By


class BasketPageLocators():
    BASKET_BUTTON = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    NAME_STORE = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    NAME_STORE_FINALLY = (By.XPATH, "//div[@class='alertinner']/strong")

class BasePageLocators_2():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")